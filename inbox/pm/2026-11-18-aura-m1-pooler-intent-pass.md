---
id: inbox-pm-aura-m1-pooler-intent-pass
agent: pm
ticket_id: 2a04d47b-6e53-4df2-a8bb-c3d63924828d
updated: 2026-11-18
status: inbox
sources:
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - ticket:88a7518f-575a-4985-a580-dff0c6be89b4
  - https://github.com/yoosungung/aura/pull/11
---

# aura M1 Pooler Intent pass → RLS kickoff

- Pooler = CloudNativePG `Pooler` transaction; DSN = `aura-pg-pooler` only
- PR #11 MERGED `9df41572`; child `88a7518f` done
- Next: RLS integration `92cccf21` (set_config + tenant isolation smoke)
