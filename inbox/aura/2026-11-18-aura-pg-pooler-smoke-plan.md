---
id: inbox-aura-pg-pooler-smoke-plan
agent: aura
ticket_id: 3f7386c8-0eb3-4133-9a0f-69a55cb4132e
updated: 2026-11-18
status: inbox
sources:
  - ticket:3f7386c8-0eb3-4133-9a0f-69a55cb4132e
  - https://github.com/yoosungung/aura/pull/9
  - https://cloudnative-pg.io/documentation/1.24/connection_pooling/
---

# Aura PG+Pooler smoke plan (M0 docs → M1 V1.1)

- Plan path: `deploy/docs/pg-pooler-smoke-plan.md` (not `services/memory/DESIGN.md` until store code lands).
- Recommend **CNPG Pooler** with `poolMode: transaction`; product lock + install remain M1. Fallback: standalone PgBouncer transaction.
- V1.1 cases: (a) DSN=pooler only (b) transaction mode (c) A→B pool reuse RLS isolation via `set_config(..., true)` (d) ban `set_config(..., false)` / direct PG.
- Script name stub only: `deploy/scripts/smoke-pg-pooler.sh` (implement in M1). Executor: `svc-memory` store.
