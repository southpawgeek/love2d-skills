#!/usr/bin/env python3
"""
Download and normalize the LÖVE API reference for a given version.

Default approach (recommended):
  - Download the upstream `love2d-community/love-api` GitHub repo as a zip
  - Load its Lua API table locally (via the `lua` interpreter)
  - Emit a deterministic, flattened markdown/text file suitable for chunking

Fallback approach:
  - Scrape the `love2d-community.github.io/love-api/` HTML bundle

Output:
  docs/love-api/LOVE_<major>_<minor>_REFERENCE.md
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import requests


def _normalize_lines(text: str) -> str:
    # Deterministic normalization:
    # - unify newlines
    # - strip trailing whitespace
    # - collapse >2 blank lines to at most 2
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in text.split("\n")]
    out: list[str] = []
    blank_run = 0
    for ln in lines:
        if ln.strip() == "":
            blank_run += 1
            if blank_run <= 2:
                out.append("")
        else:
            blank_run = 0
            out.append(ln)
    # Ensure a terminal newline for stable diffs
    return "\n".join(out).rstrip() + "\n"


def _extract_visible_text_from_html(html: str) -> str:
    from bs4 import BeautifulSoup  # imported lazily; only needed for --source html

    soup = BeautifulSoup(html, "lxml")

    # Remove non-content areas that could inject non-deterministic text.
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # Deterministic: ask for a simple newline separator.
    text = soup.get_text(separator="\n")
    return _normalize_lines(text)


def _version_marker(version: str) -> str:
    # LÖVE uses "LÖVE 11.5 Reference" in visible content.
    return f"LÖVE {version} Reference"


def _love_version_to_filename(version: str) -> str:
    major_minor = version.replace(".", "_")
    return f"LOVE_{major_minor}_REFERENCE.md"


def fetch_and_extract(url: str, timeout_s: int = 60) -> str:
    headers = {
        # Avoid trivial 403/anti-bot blocks.
        "User-Agent": "love2d-docs-offline/1.0 (local RAG tooling)",
        "Accept": "text/html,application/xhtml+xml",
    }
    resp = requests.get(url, headers=headers, timeout=timeout_s)
    resp.raise_for_status()
    return _extract_visible_text_from_html(resp.text)


def _download_github_zip(repo: str, ref: str, out_dir: Path) -> Path:
    """
    Downloads https://github.com/<repo>/archive/<ref>.zip and extracts it.
    Returns the extracted top-level directory path.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_url = f"https://github.com/{repo}/archive/{ref}.zip"
    zip_path = out_dir / f"{ref}.zip"

    headers = {
        "User-Agent": "love2d-docs-offline/1.0 (local RAG tooling)",
        "Accept": "application/zip,application/octet-stream,*/*",
    }
    resp = requests.get(zip_url, headers=headers, timeout=120)
    resp.raise_for_status()
    zip_path.write_bytes(resp.content)

    extract_dir = out_dir / "extract"
    if extract_dir.exists():
        shutil.rmtree(extract_dir)
    extract_dir.mkdir(parents=True, exist_ok=True)

    import zipfile

    with zipfile.ZipFile(str(zip_path)) as zf:
        zf.extractall(str(extract_dir))

    # GitHub zip contains a single top-level folder; detect it.
    entries = [p for p in extract_dir.iterdir() if p.is_dir()]
    if len(entries) != 1:
        raise RuntimeError(f"Unexpected zip structure; expected 1 top-level dir, got {len(entries)}")
    return entries[0]


def _emit_reference_from_repo_lua(*, extracted_top_dir: Path, out_file: Path, version: str) -> dict[str, Any]:
    """
    Generates the love-api reference markdown/text by loading the Lua API data locally.
    """
    with tempfile.TemporaryDirectory(prefix="love2d-docs-sync-") as td:
        tmp = Path(td)
        local_root = tmp / "love-api"

        if local_root.exists():
            shutil.rmtree(local_root)
        shutil.move(str(extracted_top_dir), str(local_root))

        # Lua needs a package root directory where `love-api/` exists.
        package_root = tmp

        lua_script = tmp / "render_reference.lua"
        lua_script.write_text(
            r"""
local packageRoot = arg[1]
local versionWanted = arg[2]
local outFile = arg[3]

package.path = packageRoot .. "/?.lua;" .. packageRoot .. "/?/init.lua;" .. package.path

local loveApi = require("love-api.love_api")
local extraFn = require("love-api.extra")
local api = extraFn(loveApi)

local v = api.version or versionWanted

local function compactTableText(s)
  if s == nil then return "" end
  s = tostring(s)
  s = s:gsub("\r\n", "\n")
  s = s:gsub("\n+", " ")
  s = s:gsub("^%s+", "")
  s = s:gsub("%s+$", "")
  return s
end

local function emitLine(f, s)
  f:write(s or "")
  f:write("\n")
end

local function emitSection(fullname, item, f)
  emitLine(f, fullname)
  emitLine(f, "")

  local desc = item.description or item.minidescription
  if desc and desc ~= "" then
    f:write(desc)
    f:write("\n\n")
  end

  local variants = item.variants or {}
  if #variants > 0 then
    for _, variant in ipairs(variants) do
      local args = variant.arguments or {}
      local rets = variant.returns or {}

      local argNames = {}
      for _, a in ipairs(args) do
        table.insert(argNames, a.name or "")
      end

      emitLine(f, fullname .. "(" .. table.concat(argNames, ", ") .. ")")
      emitLine(f, "")

      if #args > 0 then
        emitLine(f, "| name | type | description |")
        emitLine(f, "| --- | --- | --- |")
        for _, a in ipairs(args) do
          emitLine(
            f,
            "| " .. compactTableText(a.name) .. " | " .. compactTableText(a.type) .. " | " .. compactTableText(a.description) .. " |"
          )
        end
        emitLine(f, "")
      end

      if #rets > 0 then
        emitLine(f, "| name | type | description |")
        emitLine(f, "| --- | --- | --- |")
        for _, r in ipairs(rets) do
          emitLine(
            f,
            "| " .. compactTableText(r.name) .. " | " .. compactTableText(r.type) .. " | " .. compactTableText(r.description) .. " |"
          )
        end
        emitLine(f, "")
      end
    end
  end
end

local out = assert(io.open(outFile, "w"))
emitLine(out, "LÖVE " .. v .. " Reference")
emitLine(out, "")

local keys = {}
for fullname, _item in pairs(api.byfullname or {}) do
  if type(fullname) == "string" then
    table.insert(keys, fullname)
  end
end
table.sort(keys)

for _, fullname in ipairs(keys) do
  local item = api.byfullname[fullname]
  if item and item.what and (item.what == "function" or item.what == "method" or item.what == "callback") then
    emitSection(fullname, item, out)
    emitLine(out, "")
  end
end

out:close()
return true
            """.strip(),
            encoding="utf-8",
        )

        subprocess.run(
            ["lua", str(lua_script), str(package_root), str(version), str(out_file)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # Normalize for deterministic diffs.
        raw = out_file.read_text(encoding="utf-8")
        out_file.write_text(_normalize_lines(raw), encoding="utf-8")

        return {
            "chosenSource": "github/love-api-lua",
            "loveApiVersion": version,
        }


def probe_candidates(version: str, base_url: str) -> tuple[str, str]:
    """
    Returns (chosen_url, extracted_text).

    Strategy:
    - Try a set of likely URLs.
    - For each extracted result, validate that the version marker exists.
    """
    marker = _version_marker(version)

    candidates = [
        base_url.rstrip("/") + "/",
        base_url.rstrip("/") + f"/LOVE_{version.replace('.', '_')}_REFERENCE.md",
        base_url.rstrip("/") + f"/love-{version}.md",
        base_url.rstrip("/") + "/love-api.md",
    ]

    seen = set()
    for url in candidates:
        if url in seen:
            continue
        seen.add(url)
        try:
            extracted = fetch_and_extract(url)
        except Exception:
            continue
        if marker in extracted:
            return url, extracted

    raise RuntimeError(
        "Unable to fetch a versioned reference from the love-api site. "
        f"Tried: {candidates}. Missing marker: {marker!r}."
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="11.5", help="LÖVE version to sync (default: 11.5)")
    parser.add_argument(
        "--source",
        default="github",
        choices=["github", "html"],
        help="Where to source the LÖVE API reference from",
    )
    parser.add_argument("--github-repo", default="love2d-community/love-api", help="GitHub repo for love-api data")
    parser.add_argument("--github-ref", default="master", help="Git ref for love-api (default: master)")
    parser.add_argument(
        "--base-url",
        default="https://love2d-community.github.io/love-api",
        help="Base URL for love-api site (used when --source html)",
    )
    parser.add_argument("--out-dir", default="docs/love-api", help="Output directory")
    parser.add_argument("--metadata-out", default="docs/love-api/source_urls.json")
    parser.add_argument("--force", action="store_true", help="Overwrite existing reference files")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    out_file = out_dir / _love_version_to_filename(args.version)
    meta_file = Path(args.metadata_out)

    if out_file.exists() and not args.force:
        print(f"{out_file} already exists. Use --force to overwrite.", file=sys.stderr)
        return

    meta: dict[str, Any]

    if args.source == "github":
        with tempfile.TemporaryDirectory(prefix="love2d-docs-sync-") as td:
            tmp = Path(td)
            extracted_top = _download_github_zip(args.github_repo, args.github_ref, tmp)
            meta = {
                "version": args.version,
                "chosenSource": "github/love-api-lua",
                "repo": args.github_repo,
                "ref": args.github_ref,
            }
            meta.update(
                _emit_reference_from_repo_lua(
                    extracted_top_dir=extracted_top,
                    out_file=out_file,
                    version=args.version,
                )
            )
    else:
        chosen_url, extracted = probe_candidates(args.version, args.base_url)
        out_file.write_text(extracted, encoding="utf-8")
        meta = {
            "version": args.version,
            "chosenSource": "html/love-api",
            "chosen_url": chosen_url,
            "base_url": args.base_url,
            "note": "The site is a static HTML bundle; extraction uses visible text content.",
        }

    # Persist metadata for reproducibility.
    meta_file.parent.mkdir(parents=True, exist_ok=True)
    existing: dict[str, Any] = {}
    if meta_file.exists():
        try:
            existing = json.loads(meta_file.read_text(encoding="utf-8"))
        except Exception:
            existing = {}
    if isinstance(existing, dict):
        existing[args.version] = meta
        meta_file.write_text(json.dumps(existing, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        meta_file.write_text(json.dumps({args.version: meta}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()

