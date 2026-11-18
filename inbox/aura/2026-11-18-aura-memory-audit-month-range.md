---
id: inbox-aura-memory-audit-month-range
agent: aura
ticket_id: 85741c7b-9713-44b3-91c5-2a2fc6a5bc24
updated: 2026-11-18
status: inbox
sources:
  - ticket:85741c7b-9713-44b3-91c5-2a2fc6a5bc24
  - https://github.com/yoosungung/aura/pull/15
---

# aura memory_audit monthly RANGE + RLS

- DDL: `deploy/sql/memory_audit.sql` — parent `PARTITION BY RANGE (created_at)`; PK `(id, created_at)`; no soft delete; no FK to `memory_items`.
- RLS: FORCE + `tenant_id::text = current_setting('app.tenant_id', true)`; GUC only via `set_config(..., true)`.
- Smoke: `smoke-memory-audit.sh` attaches UTC prev/current/next months; row lands in `memory_audit_YYYY_MM`; cross-tenant hidden via pooler.
- Out of scope: audit hot 12mo DROP cadence (TTL ticket) · embeddings · svc-memory store body.
