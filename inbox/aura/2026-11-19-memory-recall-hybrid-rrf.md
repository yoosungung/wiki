---
id: inbox-aura-memory-recall-hybrid-rrf
agent: aura
ticket_id: 826b9aee-d394-462e-b3e6-9bd6e5a8ae00
updated: 2026-11-19
status: inbox
sources:
  - ticket:826b9aee-d394-462e-b3e6-9bd6e5a8ae00
  - ticket:1d669034-018b-45e0-986f-c50b24cfd735
  - wiki/RAG/HF-Infrastructure-for-Hybrid-Search-pwc.md
---

# Aura M2 recall hybrid RRF

- `aura.rpc.memory.recall` SELECT: short_term=created_at DESC; BM25(`content_tsv`/`ts_rank`) + vector(`halfvec`/`<=>`) fused with RRF k=60; graph stub empty until M4.
- Transaction: Pooler + `set_config('app.tenant_id', $1, true)` then `SET LOCAL hnsw.iterative_scan=relaxed_order` · `ef_search=40` · `max_scan_tuples=20000`; tenant WHERE in same ANN SQL (no app post-filter).
- Optional `query_embedding[]` — absent skips vector branch (live TEI non-goal). Gate: `bash deploy/scripts/check-memory-recall.sh`.
