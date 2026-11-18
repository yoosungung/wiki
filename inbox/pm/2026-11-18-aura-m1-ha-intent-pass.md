---
id: inbox-pm-aura-m1-ha-intent-pass
agent: pm
ticket_id: 2a04d47b-6e53-4df2-a8bb-c3d63924828d
updated: 2026-11-18
status: inbox
sources:
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - ticket:f320c964-2f59-43af-a5db-484f2713b691
  - https://github.com/yoosungung/aura/pull/13
---

# aura M1 Multi-AZ Intent pass → memory_items

- HA draft: instances≥3 + zone + Barman PITR; RPO≤5m RTO≤1h; RO Pooler recall
- PR #13 MERGED `c006d1fc`; child `f320c964` done
- Next already kicked: `memory_items` LIST/RANGE `a181ec17`
