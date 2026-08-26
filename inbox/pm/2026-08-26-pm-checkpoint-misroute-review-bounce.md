---
id: inbox-pm-2026-08-26-pm-checkpoint-misroute-review-bounce
agent: pm
ticket_id: 1318
updated: 2026-08-26
status: inbox
sources:
  - ticket:1318
  - ticket:1319
  - ticket:1320
  - ticket:1325
  - ticket:1326
  - wiki/Engineering/AI-Native-Engineering/Bridge-Agent-UserId-From-Config.md
---

# pm-checkpoint: Approval→Review misroute bounce

- Five Waiting-for-Approval tickets with newest ask = PR review/merge were bounced to Review + assignee pm (not human-only).
- Same-PR twins #1318/#1326 (PR #126): keep canonical #1326; reconcile #1318 after merge.
- Flow IP tickets within 30m SLA used status-board upsert only; no HC/ARC (Deploy/QA empty).
