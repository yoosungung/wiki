---
id: inbox-pm-aura-m1-rls-intent-pass
agent: pm
ticket_id: 2a04d47b-6e53-4df2-a8bb-c3d63924828d
updated: 2026-11-18
status: inbox
sources:
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - ticket:92cccf21-e2e4-48c7-b9cd-a495f1fb9d15
  - https://github.com/yoosungung/aura/pull/12
---

# aura M1 RLS V1.1 Intent pass → Multi-AZ kickoff

- smoke-pg-pooler.sh proves pooler DSN + transaction + A→COMMIT→B isolation + no session GUC
- PR #12 MERGED `a9cfe811`; child `92cccf21` done
- Next: Multi-AZ/PITR + RPO/RTO draft `f320c964`
