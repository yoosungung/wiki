---
id: inbox-qa-2026-08-05-ticket172-hangfix-smoke-partial
agent: qa
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #172 hang-fix smoke partial (`test-4e7775f`)

- Silent hang reduced: streams reach `done`.
- short Q: `error`+`done` but 16K overflow (19382>16384) after tool flood.
- local008: `done` without `sql`/`error`.
- Full 135 deferred; MDL seed still needed for pass_rate>0.
