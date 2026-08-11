---
id: inbox-pm-ticket310-spend-alert-done-regression
agent: pm
ticket_id: 310
updated: 2026-08-11
status: inbox
sources:
  - ticket:310
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
tags: ["spend-alert", "Approval", "Done-regression"]
---

# Spend-alert #310 Done without Eric evidence (again)

- After PM confirmed Waiting for Approval, #310 flipped to Done with no Eric ack/budget decision comment.
- PM reopened → Waiting for Approval + assignee Eric. Human-only cost gate; agents must not self-Done.
- Suspect remediator/cron auto-close; needs investigation outside this ticket write scope.
