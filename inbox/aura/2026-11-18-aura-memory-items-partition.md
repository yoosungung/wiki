---
id: inbox-aura-memory-items-partition
agent: aura
ticket_id: a181ec17-22c8-4179-aa68-aef3b133f047
updated: 2026-11-18
status: inbox
sources:
  - ticket:a181ec17-22c8-4179-aa68-aef3b133f047
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - https://github.com/yoosungung/aura/pull/14
---

# aura memory_items LIST + monthly RANGE + RLS

- DDL path: `deploy/sql/memory_items.sql` (not under services/memory yet — store DESIGN is a later M1 ticket).
- Partition shape: parent LIST(`memory_type`); `short_term`/`episodic` RANGE(`created_at`); `long_term`/`semantic` leaf tables.
- PK must be `(id, memory_type, created_at)` — no FK to `memory_items(id)` alone (blocks monthly DROP).
- RLS: FORCE + `tenant_id::text = current_setting('app.tenant_id', true)`; GUC only via `set_config(..., true)`.
- Live evidence: `smoke-memory-items.sh` via CNPG Pooler — cross-tenant hidden; short_term lands in `memory_items_short_term_YYYY_MM`.
- Seed months (prev/current/next UTC) are smoke-attached; TTL day counts / DROP cadence remain a separate ticket.
