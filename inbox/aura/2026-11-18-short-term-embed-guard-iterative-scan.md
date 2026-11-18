---
id: inbox-aura-short-term-embed-guard-iterative-scan
agent: aura
ticket_id: 6dfc4c4a-c066-4b88-b948-1ffa1b9c01e8
updated: 2026-11-18
status: inbox
sources:
  - ticket:6dfc4c4a-c066-4b88-b948-1ffa1b9c01e8
  - https://github.com/yoosungung/aura/pull/20
  - https://github.com/pgvector/pgvector/
---

# short_term embed 거부 + iterative_scan/ef_search M1

- Aura M1: `memory_embeddings` DDL CHECK가 short_term INSERT SoR; 앱 embed Function 사전 스킵은 M2 계약.
- Recall GUC 고정: pgvector ≥0.8 · `hnsw.iterative_scan=relaxed_order` · `ef_search=40` · `max_scan_tuples=20000`. 앱 post-filter 금지.
- 왜곡 테넌트 HNSW 픽스처(ON≥1/OFF)는 별도 티켓 — DESIGN Non-goals.
