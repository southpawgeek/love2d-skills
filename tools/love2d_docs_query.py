#!/usr/bin/env python3
"""
Query the local LÖVE docs store.

Exact symbol match:
  - load chunks.jsonl
  - find the record with matching `symbol`

Semantic fallback:
  - load FAISS index + meta.json
  - embed the query and return top-k nearest chunks

Project version detection (best-effort):
  - if --project is provided, scan Lua files for `t.version = "<...>"`
  - normalize to "major.minor"
  - fallback to 11.5
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

import numpy as np
import faiss  # type: ignore
from sentence_transformers import SentenceTransformer


EXCLUDE_DIR_NAMES = {
    ".git",
    "build",
    "dist",
    "out",
    "node_modules",
    ".next",
    ".parcel-cache",
    "vendor",
    ".venv",
    "venv",
    "__pycache__",
    "docs",
}


def parse_version_string(raw: str) -> str | None:
    s = raw.strip().strip('"').strip("'")
    # Collect all digit groups (e.g. "0.11.5" -> ["0","11","5"])
    parts = re.findall(r"\d+", s)
    if len(parts) == 2:
        return f"{int(parts[0])}.{int(parts[1])}"
    if len(parts) >= 3:
        # Commonly "0.11.5" style -> take the last two groups.
        return f"{int(parts[-2])}.{int(parts[-1])}"
    return None


def match_project_version(project_dir: Path) -> str | None:
    lua_files: list[Path] = []
    for root, dirs, files in os.walk(project_dir):
        # Prune excluded directories for speed and to avoid huge trees.
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIR_NAMES]
        for fn in files:
            if fn.endswith(".lua"):
                lua_files.append(Path(root) / fn)

    # Regex matches common assignment shapes:
    #   t.version = "11.5"
    #   t.version='11.5'
    #   t.version = 11.5
    version_assign_re = re.compile(r"\bt\.version\s*=\s*([^\n\r#]+)")

    for p in lua_files:
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        # Prefer files that define love.conf(t) first, but keep it best-effort.
        if "love.conf" not in text and "t.version" not in text:
            continue

        m = version_assign_re.search(text)
        if not m:
            continue

        candidate = m.group(1).strip()
        ver = parse_version_string(candidate)
        if ver:
            return ver

    return None


def normalize_symbol_input(s: str) -> str:
    s = s.strip()
    # Some users might pass "love.graphics.printf(...)".
    s = s.split("(", 1)[0].strip()
    return s


def excerpt(text: str, max_lines: int = 55, max_chars: int = 2500) -> str:
    lines = text.splitlines()
    out_lines = []
    total = 0
    for ln in lines:
        if len(out_lines) >= max_lines:
            break
        if total + len(ln) > max_chars:
            break
        out_lines.append(ln)
        total += len(ln) + 1
    return "\n".join(out_lines).strip()


def load_exact_chunks(chunks_path: Path) -> dict[str, dict[str, Any]]:
    if not chunks_path.exists():
        return {}
    out: dict[str, dict[str, Any]] = {}
    with chunks_path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            sym = rec.get("symbol")
            if isinstance(sym, str):
                out[sym] = rec
    return out


def load_faiss_index(index_dir: Path, version: str) -> tuple[Any, dict[str, Any]]:
    index_path = index_dir / f"love-{version}.faiss"
    meta_path = index_dir / f"love-{version}.meta.json"
    if not index_path.exists() or not meta_path.exists():
        raise FileNotFoundError(
            f"Missing FAISS artifacts for v{version}.\n"
            f"Expected: {index_path} and {meta_path}"
        )

    index = faiss.read_index(str(index_path))
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    return index, meta


def citations_line(source_url: str | None, version: str, symbol: str) -> str:
    # The love-api site doesn't guarantee stable anchor IDs for every symbol in a way
    # we can scrape reliably offline; we synthesize an "anchor" using the symbol name.
    src = source_url or "https://love2d-community.github.io/love-api/"
    return f"Citation: [{src} v{version}#{symbol}]"


def print_result(rec: dict[str, Any], version: str, full: bool) -> None:
    symbol = rec.get("symbol") or rec.get("sectionHeading") or "unknown"
    section = rec.get("sectionHeading") or symbol
    src_url = rec.get("sourceUrl")
    text = rec.get("text") or ""
    body = text if full else excerpt(text)

    print(f"Symbol: {symbol}")
    print(f"Section: {section}")
    print(citations_line(src_url, version, str(symbol)))
    print("---")
    print(body)
    print("---")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="?", help="Symbol to look up, e.g. love.graphics.printf")
    parser.add_argument("--symbol", help="Symbol to look up, e.g. love.graphics.printf")
    parser.add_argument("--project", help="Path to a LÖVE project for version detection")
    parser.add_argument("--version", help="Override LÖVE version (default: from project or 11.5)")
    parser.add_argument("--topk", type=int, default=3, help="Top-k semantic results")
    parser.add_argument("--chunks", default="docs/love-api/chunks.jsonl", help="chunks.jsonl path")
    parser.add_argument("--index-dir", default="data/love2d-docs", help="FAISS artifacts directory")
    parser.add_argument("--full", action="store_true", help="Print full chunk text")
    parser.add_argument("--dry-run", action="store_true", help="Only print resolved version and exit")
    args = parser.parse_args()

    symbol_in = args.symbol or args.query
    if not symbol_in:
        print("Provide a symbol to query, e.g. `python ... love.graphics.printf`", file=sys.stderr)
        sys.exit(2)

    symbol = normalize_symbol_input(symbol_in)

    version = args.version
    if not version and args.project:
        project_dir = Path(args.project).expanduser().resolve()
        if project_dir.exists():
            version = match_project_version(project_dir)
    version = version or "11.5"

    if args.dry_run:
        print(f"Resolved version: {version}")
        return

    chunks_path = Path(args.chunks)
    exact_chunks = load_exact_chunks(chunks_path)
    exact_rec = exact_chunks.get(symbol)

    if exact_rec is not None:
        # Exact match should be the primary signal.
        print_result(exact_rec, version, args.full)
        return

    # Semantic fallback
    try:
        index, meta = load_faiss_index(Path(args.index_dir), version)
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        print("And exact match didn't exist in chunks.jsonl.", file=sys.stderr)
        sys.exit(3)

    embedding_model = meta.get("embeddingModel", "sentence-transformers/all-mpnet-base-v2")
    model = SentenceTransformer(embedding_model)

    q = symbol_in.strip()
    q_emb = model.encode([q], convert_to_numpy=True).astype("float32")
    # Mirror build_index cosine-sim setup:
    norms = np.linalg.norm(q_emb, axis=1, keepdims=True)
    q_emb = q_emb / np.maximum(norms, 1e-12)

    # Search.
    scores, ids = index.search(q_emb, args.topk)

    vectors: list[dict[str, Any]] = meta.get("vectors", [])
    if not vectors:
        raise RuntimeError("meta.json missing `vectors` mapping.")

    for rank in range(ids.shape[1]):
        idx = int(ids[0, rank])
        if idx < 0 or idx >= len(vectors):
            continue
        rec = vectors[idx]
        print(f"Result {rank + 1}/{args.topk}")
        print_result(rec, version, args.full)


if __name__ == "__main__":
    main()

