---
id: inbox-aura-memory-ttl-partition-drop
agent: aura
ticket_id: 2649c9a0-5945-4244-b9d1-63254c8a931a
updated: 2026-11-19
status: inbox
sources:
  - ticket:2649c9a0-5945-4244-b9d1-63254c8a931a
  - https://github.com/yoosungung/aura/pull/50
---

# Aura M4: memory TTL monthly partition DROP

- Task `aura.tasks.memory.ttl` / consumer `aura_memory_ttl` DROPs expired `short_term` (14d) and `audit` (12mo) month partitions with `DROP TABLE … RESTRICT`.
- Cold `episodic` (24mo) returns `needs_archive` until archive marks `archived=true`; no silent DROP.
- Soft-delete-only cleanup forbidden; gate: `bash deploy/scripts/check-memory-ttl.sh`.
- Docs: `deploy/docs/memory-ttl-drop.md` · code: `services/memory/ttl/` · `deploy/k8s/memory-ttl/`.
