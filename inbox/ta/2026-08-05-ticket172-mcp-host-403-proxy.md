---
id: inbox-ta-2026-08-05-ticket172-mcp-host-403-proxy
agent: ta
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/modelcontextprotocol/rust-sdk/security/advisories/GHSA-89vp-x53w-74fx
  - inbox/qa/2026-08-05-ticket172-agent-ex-mcp403.md
---

# #172 nl2sql-mcp 403 was Host allowlist, not token

- QA saw backend→`http://nl2sql-mcp:8800/mcp` **403**; suspected `MCP_SHARED_TOKEN` mismatch.
- Evidence: backend and mcp pod `MCP_SHARED_TOKEN` sha256 matched; mcp logs `rejected request with disallowed Host header (DNS rebinding)` for `Host: nl2sql-mcp:8800`.
- Cause: `rmcp` ≥1.4 defaults `allowed_hosts` to loopback only; `nl2sql-mcp` uses `StreamableHttpServerConfig::default()` without `with_allowed_hosts`.
- Live unblock (nl2sql ns): nginx sidecar `host-proxy` rewrites `Host` → `127.0.0.1:8801`; mcp binds `:8801`; Service still `:8800`. Verified `initialize` HTTP 200 with `Host: nl2sql-mcp:8800`.
- Durable fix (nl2sql code/release): `MCP_ALLOWED_HOSTS` / `with_allowed_hosts(["nl2sql-mcp","nl2sql-mcp:8800",...])` then drop sidecar.
