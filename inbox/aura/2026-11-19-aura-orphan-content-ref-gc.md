---
id: inbox-aura-orphan-content-ref-gc
agent: aura
ticket_id: bb165a71-08a2-49af-828e-c5197688827e
updated: 2026-11-19
status: inbox
sources:
  - ticket:bb165a71-08a2-49af-828e-c5197688827e
  - https://github.com/yoosungung/aura/pull/31
---

# Aura orphan content_ref GC (V2.2)

- Grace **90 days** aligned with `AURA_EVENTS` retention; candidates only under `tenants/{tenant_id}/refs/` on `aura-content`.
- Task `aura.tasks.memory.object_gc` daily; batch ≤100 keys; idempotent `object-gc:{tenant|all}:{yyyy-mm-dd}`; `DeleteObject` 404=success.
- Safety: EXISTS live `metadata.content_ref` on `memory_items`/`memory_audit` → **skip**; never GC `archive/`/`bundles/`/`aura-pg`.
- L0: `deploy/docs/object-store-orphan-gc.md` · gate `check-object-store-orphan-gc.sh` · impl=M4.
