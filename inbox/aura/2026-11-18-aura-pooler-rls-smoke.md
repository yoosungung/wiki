---
id: inbox-aura-2026-11-18-pooler-rls-smoke
agent: aura
ticket_id: 92cccf21-e2e4-48c7-b9cd-a495f1fb9d15
updated: 2026-11-18
status: inbox
sources:
  - ticket:92cccf21-e2e4-48c7-b9cd-a495f1fb9d15
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - https://github.com/yoosungung/aura/pull/12
---

# Aura V1.1 Pooler + RLS smoke

- Fixture: `deploy/k8s/pg-pooler/rls-smoke-fixture.sql` — `FORCE ROW LEVEL SECURITY` + policy on `app.tenant_id`.
- Live gate: `bash deploy/scripts/smoke-pg-pooler.sh` via DSN host `aura-pg-pooler…` only.
- Proof: tenant A insert → COMMIT → tenant B on same client (and second session) never sees A rows; GUC clears after COMMIT (`set_config(..., true)`).
- Static: `SMOKE_PG_POOLER_STATIC=1` covers forbid `set_config(..., false)` / `SET app.tenant_id` scan + manifest gate.
- Non-goal kept: production `memory_*` DDL / `services/memory` store MQT (later M1).
