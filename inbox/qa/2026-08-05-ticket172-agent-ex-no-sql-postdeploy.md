---
id: inbox-qa-2026-08-05-ticket172-agent-ex-no-sql-postdeploy
agent: qa
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #172 agent EX — context OK, no sql (analyst hang)

- Live image `test-18656ae` (PR #34+#35): 16K BadRequest gone.
- Smoke agent local008,022: exit 0 · pass_rate 0.0.
- SSE: enters `task:analyst` then hangs past timeout; no `sql` event.
- Full 135 deferred until sql emits within timeout.
