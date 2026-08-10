---
id: inbox-nl2sql-ticket415-tool-result-ok
agent: nl2sql
ticket_id: 415
updated: 2026-08-10
status: inbox
sources:
  - ticket:415
  - https://chatforest.com/guides/mcp-error-handling-explained/
  - https://developers.cloudflare.com/agents/model-context-protocol/protocol/tools/
---

# #415 tool_result.ok reflects MCP failure

- Chat SSE always set `tool_result.ok: true`; MCP `CallToolResult.error` bodies (`{"error":{code,message}}`) and `isError`/`is_error` must map to `ok:false`.
- Helper `_tool_result_payload` in `routers/chat.py`; failure summary is `{code, message}` one-liner for UI/debug.
- Scope stays SSE truthfulness only — empty-SQL root cause remains #391.
