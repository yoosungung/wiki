---
id: inbox-pm-ticket415-tool-result-ok
agent: pm
ticket_id: 415
updated: 2026-08-10
status: inbox
sources:
  - ticket:415
  - ticket:391
  - https://py.sdk.modelcontextprotocol.io/v2/servers/handling-errors/
  - https://www.mcpscoreboard.com/build/guides/error-handling/
---

# #415 tool_result ok:True triage

- AA Med smell `err.swallowed` at `chat.py` tool_result always `ok: True` — UI/debug hide MCP tool failures.
- MCP contract: surface failure via `isError`/`ok:false` + one-line code/message; never return error text as success.
- Scope vs #391: #415 = SSE/conversation truthfulness of tool_result; #391 = empty warehouse_sql root-cause (Blocked). Do not merge scopes.
- Owner: nl2sql; boy-scout fix + unit test that failed tool yields ok:false.
