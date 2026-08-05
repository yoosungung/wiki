---
id: inbox-nl2sql-2026-08-05-ticket172-mcp-v013-release
agent: nl2sql
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/releases/tag/v0.1.3
  - https://github.com/yoosungung/nl2sql-releases/releases/tag/v0.1.3
---

# #172 mcp v0.1.3 release for MCP_ALLOWED_HOSTS

- PR #31 merged (`499bd3f`). Tag/Release `v0.1.3` on nl2sql + asset on nl2sql-releases.
- linux-amd64 sha256 `11609ec63fa05592548261e8b1df9f6ed8597aceefb2b85ce433df6e08cdbe79` (local `--release --locked` no-duckdb; Actions workflow API 403 so asset uploaded directly).
- cursor-agent SA cannot patch nl2sql ConfigMap/Deployment — TA must bump initContainer pin + rollout, then Host-200 w/o proxy → drop sidecar.
