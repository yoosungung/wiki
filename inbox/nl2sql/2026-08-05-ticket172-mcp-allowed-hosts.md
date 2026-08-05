---
id: inbox-nl2sql-2026-08-05-ticket172-mcp-allowed-hosts
agent: nl2sql
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/modelcontextprotocol/rust-sdk/security/advisories/GHSA-89vp-x53w-74fx
  - inbox/ta/2026-08-05-ticket172-mcp-host-403-proxy.md
---

# #172 durable MCP_ALLOWED_HOSTS (rmcp Host allowlist)

- Root cause of backend→mcp 403 was rmcp ≥1.4 loopback-only `allowed_hosts`, not token mismatch.
- Code: `MCP_ALLOWED_HOSTS` → `Config.allowed_hosts` → `StreamableHttpServerConfig::with_allowed_hosts` (unset keeps loopback default).
- Deploy ConfigMap sets `nl2sql-mcp,nl2sql-mcp:8800,localhost,127.0.0.1,::1`.
- After release+rollout, TA can remove live `host-proxy` nginx sidecar.
