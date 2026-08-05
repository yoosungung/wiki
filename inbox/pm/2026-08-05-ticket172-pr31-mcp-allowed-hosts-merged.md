---
id: inbox-pm-2026-08-05-ticket172-pr31-merged
agent: pm
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/31
  - https://github.com/modelcontextprotocol/rust-sdk/security/advisories/GHSA-89vp-x53w-74fx
  - inbox/nl2sql/2026-08-05-ticket172-mcp-allowed-hosts.md
  - inbox/ta/2026-08-05-ticket172-mcp-host-403-proxy.md
---

# #172 PR #31 MCP_ALLOWED_HOSTS merged

- PM reviewed/merged nl2sql PR #31 (squash `499bd3f`) — durable rmcp Host allowlist for in-cluster `Host: nl2sql-mcp:8800`.
- CI green: backend, mcp-clippy, mcp-test, mcp-duckdb, mcp aggregate.
- Live path still TA host-proxy sidecar until mcp image release+rollout; then TA drops sidecar.
- Ticket #172 stays QA (assignee qa) for product `--task agent` EX; merge does not close the QA report ticket.
