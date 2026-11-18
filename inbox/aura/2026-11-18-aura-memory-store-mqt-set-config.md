---
id: inbox-aura-memory-store-mqt-set-config
agent: aura
ticket_id: 1c796f58-89e0-457e-8c19-e73a69fc2160
updated: 2026-11-18
status: inbox
sources:
  - ticket:1c796f58-89e0-457e-8c19-e73a69fc2160
  - https://blog.paulserban.eu/post/row-level-security-and-connection-pooling-closing-postgress-multi-tenant-leak-vector/
---

# svc-memory store MQT + transaction-local set_config

- `withTenantTx`: BEGIN → `set_config('app.tenant_id', $1, true)` → work → COMMIT; never `false` / session SET (Pooler transaction pooling).
- MQT: `aura.tasks.memory.store` → `aura.events.memory.stored` / `.store.error`; consumer `aura_memory_store`; `minReplicaCount=0`.
- Static gate: `bash deploy/scripts/check-memory-store.sh` (+ handler/tenant-tx selftests). Live pg UPSERT = follow-up on same helper.
