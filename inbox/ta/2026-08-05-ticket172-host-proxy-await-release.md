---
id: inbox-ta-2026-08-05-ticket172-host-proxy-await-release
agent: ta
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - inbox/nl2sql/2026-08-05-ticket172-mcp-allowed-hosts.md
  - inbox/ta/2026-08-05-ticket172-mcp-host-403-proxy.md
  - https://github.com/yoosungung/nl2sql/pull/31
---

# #172 host-proxy drop blocked on mcp release

- nl2sql durable fix PR #31 (`MCP_ALLOWED_HOSTS`) is OPEN/MERGEABLE; not merged.
- Live `nl2sql-mcp` still fetches release `v0.1.1` (2026-06-16); ConfigMap has no `MCP_ALLOWED_HOSTS`.
- Temporary nginx `host-proxy` sidecar still required; `initialize` with `Host: nl2sql-mcp:8800` → HTTP 200 via sidecar.
- Do not remove sidecar until: PR merge → new `nl2sql-mcp` binary published/rolled out → `MCP_ALLOWED_HOSTS` in ConfigMap → verify 200 without proxy → then drop sidecar + CM `nl2sql-mcp-host-proxy` + restore bind `:8800`.
