---
id: inbox-ta-nl2sql-mcp-roll-v013
agent: ta
ticket_id: 590
updated: 2026-08-13
status: inbox
sources:
  - ticket:590
  - https://github.com/yoosungung/nl2sql/pull/73
---

# nl2sql-mcp ticket-triggered roll (v0.1.3)

- Init 404 fixed by pinning fetch to `v0.1.3` + sha `3acba222…1817a`; annotation `nl2sql.io/mcp-binary=v0.1.3/nl2sql-mcp-linux-amd64`.
- Use `Recreate` strategy for `nl2sql-mcp` — RWO PVC `nl2sql-mcp-metadata` cannot dual-mount during RollingUpdate surge.
- v0.1.3 libgit2 fails credential-callback auth (`too many redirects or authentication replays`) when remote URL has no userinfo; workaround: Secret keys `MCP_METADATA_GIT_REMOTE` / `METADATA_GIT_REMOTE` with `http://git:<token>@…` (ConfigMap stays plain). curl basic-auth to git-http-server returns 200 with same token.
- Do not full `apply -k` test overlay blindly — overlay backend tag may differ from live tip (`test-42c2eb1`).
