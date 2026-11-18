---
id: inbox-pm-aura-m1-embeddings-intent-pass
agent: pm
ticket_id: 2a04d47b-6e53-4df2-a8bb-c3d63924828d
updated: 2026-11-18
status: inbox
sources:
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - ticket:0d7a4200-bad4-4b45-9b25-def2542064f2
  - https://github.com/yoosungung/aura/pull/19
---

# aura M1 memory_embeddings Intent pass → short_term embed guard

- LIST(model_key)+halfvec HNSW + ATTACH→DETACH runbook; PR #19 MERGED `3f786705`
- Next: short_term embed reject + pgvector≥0.8 / iterative_scan DESIGN `6dfc4c4a`
