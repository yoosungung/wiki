---
id: inbox-pm-aura-m1-memory-items-intent-pass
agent: pm
ticket_id: 2a04d47b-6e53-4df2-a8bb-c3d63924828d
updated: 2026-11-18
status: inbox
sources:
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - ticket:a181ec17-22c8-4179-aa68-aef3b133f047
  - https://github.com/yoosungung/aura/pull/14
---

# aura M1 memory_items Intent pass → memory_audit

- LIST(memory_type)+short/episodic monthly RANGE+FORCE RLS; smoke PASS
- PR #14 MERGED `8cd6f8a6`; child `a181ec17` done
- Next: memory_audit monthly RANGE `85741c7b` (already kicked)
