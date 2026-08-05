---
id: inbox-nl2sql-2026-08-05-ticket172-stop-tool-flood-analyst-error
agent: nl2sql
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - inbox/qa/2026-08-05-ticket172-hangfix-smoke-partial.md
---

# #172 stop tool flood + analyst_no_sql SSE

- openai HarnessProfile excludes FS tools (`edit_file`/`write_file`/…) — gemma ~214-call flood → 16K.
- recursion_limit 40 overrides deepagents default 9999.
- analyst task without SQL → SSE `error`(`analyst_no_sql`) then `done`.
