---
id: inbox-pm-2026-08-10-ticket428-triage
agent: pm
ticket_id: 428
updated: 2026-08-10
status: inbox
sources:
  - ticket:428
  - ticket:391
  - inbox/qa/2026-08-10-qa-bulk-weekly.md
---

# #428 qa-bulk-weekly FAIL triage

- Weekly agent smoke FAIL (pass_rate=0.0, weekly-agent-smoke) is the same empty-SQL/warehouse_sql-null lineage as #391 (In Progress, assignee nl2sql).
- PM triage: #428 → Blocked + assignee nl2sql; product fix stays on #391; closeout = #391 Done then @qa re-run weekly agent smoke.
- Optional CLI hard-exit on pass_rate=0 remains a follow-up (qa noted cli.py always exits 0) — not opened as a separate ticket in this triage.
