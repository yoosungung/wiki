---
id: inbox-pm-2026-08-12-pm-checkpoint-563-dead-by-timeout
agent: pm
ticket_id: 563
updated: 2026-08-12
status: inbox
sources:
  - ticket:563
  - skill:leantime-pm §2.6 #14 closed-loop
---

# pm-checkpoint #563 dead-by-timeout terminal

- Flow-active only #563 Deploying Test assignee=ta; IP/Review/QA/Prod empty.
- Silence clock: last assignee Outcome #2152 @ 08:39Z; HC #2802 @ 10:51Z does not reset.
- ≥1h after HC + assignee=ta → skip ARC → dead-by-timeout → cycle=1 terminal Approval + admin (eric type:human).
- Status board #2142 upserted ladder_rung=terminal; one actionable @eric add_comment this run.
