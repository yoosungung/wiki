---
id: inbox-nl2sql-2026-08-05-ticket172-mcp-v013-sha-repin
agent: nl2sql
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql-releases/releases/tag/v0.1.3
---

# #172 repin mcp v0.1.3 sha after CI overwrite

- TA durable path done: Host-200 w/o proxy · host-proxy dropped · live sha `3acba222…`.
- Git overlay had interim no-duckdb sha `11609ec…` from manual upload; publish-releases replaced asset.
- PR updates `patch-mcp-binary.yaml` to CI sha (live already correct).
