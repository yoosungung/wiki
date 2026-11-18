---
id: inbox-aura-memory-items-list-range-rls
agent: aura
ticket_id: a181ec17-22c8-4179-aa68-aef3b133f047
updated: 2026-11-18
status: inbox
sources:
  - ticket:a181ec17-22c8-4179-aa68-aef3b133f047
  - repo:yoosungung/aura
---

# Aura memory_items LIST + monthly RANGE + RLS

- DDL: `deploy/sql/memory_items.sql` — parent `PARTITION BY LIST (memory_type)`; short_term/episodic `RANGE(created_at)`; long_term/semantic leaf.
- RLS: `FORCE` + `tenant_id::text = current_setting('app.tenant_id', true)` (Pooler transaction `set_config(..., true)`).
- Gates: `check-memory-items.sh` (static) · `smoke-memory-items.sh` (pooler live seeds UTC prev/current/next months).
- Out of scope here: memory_audit · embeddings/HNSW · svc-memory store body · TTL DROP job numbers in DESIGN.
