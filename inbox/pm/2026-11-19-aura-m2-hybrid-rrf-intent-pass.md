---
id: inbox-pm-aura-m2-hybrid-rrf-intent-pass
agent: pm
ticket_id: 826b9aee-d394-462e-b3e6-9bd6e5a8ae00
updated: 2026-11-19
status: inbox
sources:
  - ticket:826b9aee-d394-462e-b3e6-9bd6e5a8ae00
  - ticket:1d669034-018b-45e0-986f-c50b24cfd735
  - https://github.com/yoosungung/aura/pull/28
---

# Aura M2 recall hybrid RRF — Intent pass

- PR#28 merged (`10fc47dd`): short_term recent + BM25/vector RRF (`k=60`) + graph stub on `aura.rpc.memory.recall`.
- Contract checks: `SET LOCAL hnsw.iterative_scan/ef_search/max_scan_tuples`; vector SQL keeps `tenant_id` in-WHERE; Pooler + `set_config(..., true)`.
- Next M2 child: Agent 주입 계약 (`e9ef0dd8`); Object Store / GC still backlog.
