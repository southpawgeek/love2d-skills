#!/usr/bin/env python3
"""
Build a local FAISS index for offline LÖVE docs retrieval.

Reads:
  docs/love-api/chunks.jsonl

Writes:
  data/love2d-docs/love-<version>.faiss
  data/love2d-docs/love-<version>.meta.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import faiss  # type: ignore
from sentence_transformers import SentenceTransformer
from tqdm import tqdm


def l2_normalize(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    return x / np.maximum(norms, eps)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunks", default="docs/love-api/chunks.jsonl", help="Input JSONL chunks file")
    parser.add_argument("--index-dir", default="data/love2d-docs", help="Output directory")
    parser.add_argument("--version", default="11.5", help="LÖVE version (default: 11.5)")
    parser.add_argument("--model", default="sentence-transformers/all-mpnet-base-v2", help="Embedding model")
    parser.add_argument("--batch-size", type=int, default=32, help="Embedding batch size")
    parser.add_argument("--max-chunks", type=int, default=0, help="Optional cap for debugging (0 = no cap)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing index")
    args = parser.parse_args()

    chunks_path = Path(args.chunks)
    if not chunks_path.exists():
        print(f"Missing chunks file: {chunks_path}", file=sys.stderr)
        sys.exit(2)

    index_dir = Path(args.index_dir)
    index_dir.mkdir(parents=True, exist_ok=True)

    out_index = index_dir / f"love-{args.version}.faiss"
    out_meta = index_dir / f"love-{args.version}.meta.json"

    if out_index.exists() and out_meta.exists() and not args.force:
        print(f"Index already exists for v{args.version}. Use --force to rebuild.", file=sys.stderr)
        return

    records: list[dict] = []
    texts: list[str] = []
    with chunks_path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            records.append(rec)
            texts.append(rec["text"])
            if args.max_chunks and len(texts) >= args.max_chunks:
                break

    if not texts:
        raise RuntimeError("No chunks loaded; cannot build index.")

    print(f"Loaded {len(texts)} chunks. Embedding using {args.model}...")
    model = SentenceTransformer(args.model)

    # SentenceTransformer returns float32 by default, but we cast to ensure FAISS compatibility.
    embeddings = model.encode(
        texts,
        batch_size=args.batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=False,
    ).astype("float32")

    # Cosine similarity via inner product:
    # - L2-normalize vectors
    # - use IndexFlatIP
    embeddings = l2_normalize(embeddings)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    faiss.write_index(index, str(out_index))

    meta = {
        "version": args.version,
        "embeddingModel": args.model,
        "numVectors": len(records),
        "dimension": dim,
        # FAISS id -> chunk record. Keep it compact but include text for citations.
        "vectors": [
            {
                "symbol": r.get("symbol"),
                "sectionHeading": r.get("sectionHeading", r.get("symbol")),
                "sourceUrl": r.get("sourceUrl"),
                "text": r.get("text"),
            }
            for r in records
        ],
    }

    out_meta.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote index: {out_index}")
    print(f"Wrote meta : {out_meta}")


if __name__ == "__main__":
    main()

