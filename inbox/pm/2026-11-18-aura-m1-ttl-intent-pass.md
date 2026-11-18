---
id: inbox-pm-aura-m1-ttl-intent-pass
agent: pm
ticket_id: 2a04d47b-6e53-4df2-a8bb-c3d63924828d
updated: 2026-11-18
status: inbox
sources:
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - ticket:06ca1e75-d8b6-4977-aa63-30dc13abe3e8
  - https://github.com/yoosungung/aura/pull/16
---

# aura M1 TTL policy Intent pass → memory_nodes/edges

- TTL fixed: short_term 14d / episodic 24mo / audit 12mo; daily DROP; aura.tasks.memory.ttl
- PR #16 MERGED `0bc8ef54`; child `06ca1e75` done
- Next: memory_nodes/edges + RLS `fa6351fa`
