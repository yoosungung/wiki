---
id: inbox-aura-memory-audit-month-range
agent: aura
ticket_id: 85741c7b-9713-44b3-91c5-2a2fc6a5bc24
updated: 2026-11-18
status: inbox
sources:
  - ticket:85741c7b-9713-44b3-91c5-2a2fc6a5bc24
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - https://github.com/yoosungung/aura/pull/15
---

# aura memory_audit 월 RANGE + RLS

- `memory_audit`는 `PARTITION BY RANGE (created_at)` · PK `(id, created_at)` · soft delete/`valid_until` 없음(파티션 DROP SoR).
- FORCE RLS + `tenant_id::text = current_setting('app.tenant_id', true)`; session GUC·`memory_items` FK 금지.
- 검증: `check-memory-audit.sh` / `smoke-memory-audit.sh` (pooler DSN · UTC 월 ATTACH · `b_sees_a=0`).
- DDL: `deploy/sql/memory_audit.sql` (aura PR#15).
