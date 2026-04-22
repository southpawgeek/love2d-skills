# love2d-skills

Local LÖVE 2D API docs with FAISS vector search and symbol-level citations.

## What is this?

A self-contained documentation index for the LÖVE 2D game engine. It chunks the official LÖVE API reference into symbol-addressable records, builds a FAISS vector index for semantic retrieval, and serves queries with `Citation:`-lined snippets — designed to feed grounded context into LLMs via Cursor, Crush, or CLI.

## Quick start

```bash
python3 -m pip install -r requirements.txt
```

## Architecture

```
docs/love-api/
  ├── LOVE_11_5_REFERENCE.md   # Flattened API reference (raw)
  └── chunks.jsonl             # Chunked, symbol-addressable records

data/love2d-docs/
  ├── love-11.5.faiss          # FAISS vector index
  └── love-11.5.meta.json      # Index metadata (version, model, etc.)

tools/
  ├── love2d_docs_sync.py       # Fetch upstream API reference
  ├── love2d_docs_chunk.py      # Split reference into chunks
  ├── love2d_docs_build_index.py # Build FAISS index
  └── love2d_docs_query.py      # Query (exact match + semantic fallback)
```

## Build pipeline

```bash
# 1. Sync upstream LÖVE API reference
python tools/love2d_docs_sync.py --version 11.5

# 2. Chunk into symbol-addressable records
python tools/love2d_docs_chunk.py \
  --input docs/love-api/LOVE_11_5_REFERENCE.md \
  --output docs/love-api/chunks.jsonl

# 3. Build FAISS vector index
OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python tools/love2d_docs_build_index.py \
  --chunks docs/love-api/chunks.jsonl \
  --index-dir data/love2d-docs \
  --version 11.5 \
  --model sentence-transformers/all-mpnet-base-v2
```

## Query

Exact symbol lookup:

```bash
python tools/love2d_docs_query.py love.graphics.printf
```

Semantic fallback (top-k nearest chunks with citations):

```bash
python tools/love2d_docs_query.py "how to draw text"
```

Project-aware version detection:

```bash
python tools/love2d_docs_query.py \
  --project /path/to/your/love-project \
  love.graphics.printf
```

## How it fits with LLMs

This repo provides the **retrieval** layer of RAG:

1. Query the index via CLI or the `love2d_docs_query` tool
2. Feed the returned chunks (with `Citation:` lines) into your LLM as context
3. The LLM generates grounded answers referencing the exact API docs

Integration points:
- **Crush**: Uses `AGENTS.md` grounding instructions to query docs before answering
- **Cursor**: Can be wired into a custom tool or skill for inline doc lookups
- **CLI**: Direct query output for manual reference

## Troubleshooting

- **Missing FAISS index**: Re-run the build pipeline (step 3 above)
- **Index build crash** (segfault/exit code 139): Use `OMP_NUM_THREADS=1 MKL_NUM_THREADS=1` and try `--batch-size 8`
- **Exact lookup fails**: Ensure `chunks.jsonl` was generated from the same reference version
- **Semantic retrieval fails**: Verify `data/love2d-docs/love-*.faiss` and `love-*.meta.json` exist
