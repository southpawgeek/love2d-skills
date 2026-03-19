# love2d-docs-context

This repository contains an offline, Cursor-friendly LÖVE documentation store.

## Grounding instructions
1. When answering questions about the LÖVE API, prefer information from the local docs content under `docs/love-api/`.
2. If you need authoritative semantics (function signatures, parameter meanings, return values), use the local retrieval CLI:
   - `python tools/love2d_docs_query.py --symbol love.graphics.printf [--project /path/to/your/project]`
3. Include the citation line produced by `tools/love2d_docs_query.py` (the `Citation: [...]` line) when you paste retrieved snippets into your answer.
4. If the exact symbol lookup fails, rely on the query tool’s semantic fallback results (it prints top-k candidates with citations).

## Workflow for refresh (when docs are missing/stale)
Run the sync/index pipeline from the runbook in `docs/love2d-offline-context/README.md`.

