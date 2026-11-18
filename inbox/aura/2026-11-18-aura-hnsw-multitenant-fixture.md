---
id: inbox-aura-hnsw-multitenant-fixture
agent: aura
ticket_id: fbed0ce9-7b83-42ab-bdbc-e71fb7aa71fa
updated: 2026-11-18
status: inbox
sources:
  - ticket:fbed0ce9-7b83-42ab-bdbc-e71fb7aa71fa
  - https://github.com/yoosungung/aura/pull/21
  - https://github.com/pgvector/pgvector
---

# Aura M1 multitenant HNSW fixture (ON≥1 / OFF=0)

- L2 fixture (`halfvec_l2_ops`, A=2000 near origin, B at ~0.2): `iterative_scan=off` → B=0; `relaxed_order` → B≥1. Forces HNSW via `enable_seqscan=off` on a PK-free fixture table.
- Production path stays `halfvec_cosine_ops`. Same skew under cosine showed OFF=0 **and** ON=0 (iterative_scan did not recover B) on pgvector 0.8.7 — gap logged; T1/T2 candidate, schema not applied.
- Competing btree/PK on partitioned `memory_embeddings` makes the planner prefer exact filter+sort; fixture table avoids that for ANN regression.
