---
id: inbox-aura-memory-embed-mqt-short-term-skip
agent: aura
ticket_id: fdee9181-52f2-4678-810c-cecf67fc3917
updated: 2026-11-19
status: inbox
sources:
  - ticket:fdee9181-52f2-4678-810c-cecf67fc3917
  - https://github.com/yoosungung/aura/pull/26
---

# Aura M2 embed MQT — short_term skip

- `aura.tasks.memory.embed`: `short_term` → `skipped_short_term` (PG/`set_config` 미시도); episodic/long_term/semantic → `withTenantTx` + active `model_key` stub.
- HNSW = embed 소유; BM25 = store `content_tsv` GENERATED 적격 (`indexes.hnsw/bm25`).
- 정적 게이트: `bash deploy/scripts/check-memory-embed.sh` · selftest `services/memory/embed/handler.selftest.js`.
- Non-goals this slice: live TEI · real halfvec INSERT · recall.
