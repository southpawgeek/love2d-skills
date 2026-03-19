# Offline LÖVE Docs (FAISS + citations)

This folder documents how to build the local LÖVE API store used by this repo’s tooling.

## Prerequisites

```bash
python3 -m pip install -r requirements.txt
```

## Build the offline docs store

1. Sync the raw LÖVE 11.5 reference into `docs/love-api/`

```bash
# Note: `love2d_docs_sync.py` defaults to `--source github` (uses the upstream love-api Lua table)
python tools/love2d_docs_sync.py --version 11.5
```

2. Chunk it into symbol-addressable records (`docs/love-api/chunks.jsonl`)

```bash
python tools/love2d_docs_chunk.py --input docs/love-api/LOVE_11_5_REFERENCE.md --output docs/love-api/chunks.jsonl
```

3. Build the FAISS vector index for semantic retrieval

```bash
# Note: for stability on macOS/Python builds, force single-threading for embedding/BLAS.
OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python tools/love2d_docs_build_index.py \
  --chunks docs/love-api/chunks.jsonl \
  --index-dir data/love2d-docs \
  --version 11.5 \
  --model sentence-transformers/all-mpnet-base-v2
```

## Query examples

Exact symbol lookup:

```bash
python tools/love2d_docs_query.py love.graphics.printf --index-dir data/love2d-docs --chunks docs/love-api/chunks.jsonl
```

With project-aware version detection:

```bash
python tools/love2d_docs_query.py \
  --project /path/to/your/love-project \
  love.graphics.printf
```

If exact lookup fails, the tool falls back to semantic FAISS search automatically and prints top-k results with `Citation: [...]` lines.

## Troubleshooting

- If semantic retrieval fails, ensure the FAISS artifacts exist:
  - `data/love2d-docs/love-11.5.faiss`
  - `data/love2d-docs/love-11.5.meta.json`
- If the FAISS index build crashes (e.g. segfault/exit code 139), re-run using:
  - `OMP_NUM_THREADS=1 MKL_NUM_THREADS=1`
  - a smaller `--batch-size` (e.g. `--batch-size 8`)
- If exact lookup fails, ensure `docs/love-api/chunks.jsonl` was generated from the same reference version.

