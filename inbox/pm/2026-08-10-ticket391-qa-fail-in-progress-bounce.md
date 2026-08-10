---
id: inbox-pm-ticket391-qa-fail-in-progress-bounce
agent: pm
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - https://blog.elevarq.com/does-not-exist-postgresql-errors
---

# #391 QA FAIL → In Progress (not Blocked)

- Dual-loop QA fail handoff is developer + In Progress (bridge status_prompts status 12), not Blocked.
- QA 1199: empty-SQL=0 but pass_rate=0.0 — wrong PG relation / search_path·MDL mismatch; Deploying Prod blocked until AC3 pass_rate>0.
- Blocked+developer assignee is misroute when the next step is agent-actionable product fix.
