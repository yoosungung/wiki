---
id: inbox-aura-memory-items-upsert
agent: aura
ticket_id: a2fa7813-38e6-41a2-8b4b-8c26dcc06694
updated: 2026-11-28
status: inbox
sources:
  - ticket:a2fa7813-38e6-41a2-8b4b-8c26dcc06694
  - wiki/Engineering/AI-Native-Engineering/Aura-M1-Memory-Pg-Pooler-Rls.md
---

# memory_items INSERT/UPSERT (store module)

- Rust `services/memory/src/store.rs`: `with_tenant_tx` → `INSERT INTO memory_items … ON CONFLICT (id, memory_type, created_at) DO UPDATE`.
- `content` 인라인 또는 `content_ref`→`metadata.content_ref` (빈 content 허용); `content_tsv`는 GENERATED — INSERT 컬럼 금지.
- 단위 경로=`RecordingClient`; live Pooler/sqlx DSN은 후속. capture.rs에 SQL 인라인 금지(게이트).
- Gate: `bash deploy/scripts/check-memory-store.sh`.
