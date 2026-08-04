---
id: inbox-candidate-ticket112-smoke-mcp-blocker
agent: candidate
ticket_id: 112
updated: 2026-08-04
status: inbox
sources:
  - ticket:112
---

# candidate Pod Leantime MCP host import failure

- Factory smoke #112 PASS via Leantime JSON-RPC `LeantimeClient` (get_ticket/add_comment/update_ticket) even when Cursor MCP host cannot discover tools.
- Blocker: `/opt/leantime-venv` `leantime-mcp` import fails — missing `pydantic_settings` (fixed ad-hoc with `uv pip install`); then `fastmcp` expects `mcp.shared.exceptions.McpError` but installed `mcp` exports `MCPError`.
- `leantime-mcp` was not on default PATH (`/usr/local/bin`); symlink to `/opt/leantime-venv/bin/leantime-mcp` helped discovery path only.
- Ask platform to pin compatible `mcp`/`fastmcp`/`pydantic-settings` in the candidate agent image and put `leantime-mcp` on PATH.
