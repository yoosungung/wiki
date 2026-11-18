---
id: inbox-aura-memory-recall-hybrid-rrf
agent: aura
ticket_id: 826b9aee-d394-462e-b3e6-9bd6e5a8ae00
updated: 2026-11-19
status: inbox
sources:
  - ticket:826b9aee-d394-462e-b3e6-9bd6e5a8ae00
  - ticket:1d669034-018b-45e0-986f-c50b24cfd735
---

# Aura recall hybrid RRF (M2)

- `aura.rpc.memory.recall` success mode is `hybrid_rrf` (not deploy stub).
- short_term = `ORDER BY created_at DESC` only (no HNSW); slot budget default 4.
- BM25 (`content_tsv`) + vector (`halfvec <=>`) fused with RRF k=60; graph is stub until M4.
- Every recall tx: `set_config('app.tenant_id', $1, true)` + `SET LOCAL hnsw.iterative_scan/ef_search=40/max_scan_tuples=20000`.
- tenant_id must stay in the same vector SQL — app post-filter forbidden (small-tenant recall=0 trap).
- `query_embedding` absent → skip vector branch (live TEI non-goal); BM25 + short_term still run.
- Gate: `bash deploy/scripts/check-memory-recall.sh`.
