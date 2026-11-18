---
id: inbox-aura-memory-store-mqt
agent: aura
ticket_id: 1c796f58-89e0-457e-8c19-e73a69fc2160
updated: 2026-11-18
status: inbox
sources:
  - ticket:1c796f58-89e0-457e-8c19-e73a69fc2160
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
---

# aura svc-memory store MQT + set_config

- M1: `services/memory/DESIGN.md` + `deploy/k8s/memory-store` MQT (`aura.tasks.memory.store` / `aura_memory_store` / stored|error).
- Every store tx: `SELECT set_config('app.tenant_id', $1, true)` via `withTenantTx` — never `false` / session SET.
- DSN host = `aura-pg-pooler` only. Gate: `bash deploy/scripts/check-memory-store.sh`.
- Non-goals kept: embed/recall body, live pg Pool packaging, TEI.
