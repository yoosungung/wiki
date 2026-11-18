---
id: inbox-aura-pooler-rls-smoke
agent: aura
ticket_id: 92cccf21-e2e4-48c7-b9cd-a495f1fb9d15
updated: 2026-11-18
status: inbox
sources:
  - ticket:92cccf21-e2e4-48c7-b9cd-a495f1fb9d15
  - ticket:88a7518f-575a-4985-a580-dff0c6be89b4
---

# CNPG Pooler + RLS smoke (V1.1)

- Fixture `deploy/k8s/pg-pooler/rls-smoke-fixture.sql`: `FORCE ROW LEVEL SECURITY` + `app.tenant_id` policy; DDL wrapped in one txn (PgBouncer transaction pooling).
- Live `smoke-pg-pooler.sh`: A→COMMIT→B via pooler Service; cross-tenant hidden; `set_config(..., true)` clears after COMMIT; static forbid `set_config(..., false)`.
- Static gate: `SMOKE_PG_POOLER_STATIC=1`.
