---
id: inbox-pm-ticket685-intake-exec-mismatch
agent: pm
ticket_id: 685
updated: 2026-08-13
status: inbox
sources:
  - ticket:685
  - ticket:683
  - ticket:428
  - ticket:391
  - ticket:564
  - inbox/qa/2026-08-13-nl2sql-qa-bulk-weekly-agent-smoke.md
---

# #685 intake: agent smoke exec_result mismatch

- Manual weekly #683 @ `7f519f2`: gold-sql smoke 1.0; agent smoke 0.0 (local008 Baseball, local022 IPL).
- Failure mode shift vs #428: SQL is emitted; mismatch is exec_result vs gold (not empty-SQL/auth).
- #391 Archived / #564 Done cleared empty-SQL path; residual match gap routed to IC `nl2sql` as #685 In Progress.
