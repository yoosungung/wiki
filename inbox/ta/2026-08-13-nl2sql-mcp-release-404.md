---
id: inbox-ta-nl2sql-mcp-release-404
agent: ta
ticket_id: 590
updated: 2026-08-13
status: inbox
sources:
  - ticket:590
  - https://github.com/yoosungung/nl2sql-releases/releases/download/test-eb4bc95/nl2sql-mcp-linux-amd64
---

# nl2sql-mcp init release 404

- Deployment `nl2sql/nl2sql-mcp` init `fetch-mcp-binary` curls `test-eb4bc95/nl2sql-mcp-linux-amd64` → HTTP 404 (exit 22); RS `57d45bb4cf` ProgressDeadlineExceeded.
- Old Ready replica still serves `:8800` (`/health` ok via ClusterIP).
- HEAD 302 OK: `v0.1.3`, `prod-841059f`, `v0.1.1`. Missing: `test-eb4bc95`, `test-42c2eb1`.
- Fix path: republish asset or retarget init URL+sha256, then ticket-triggered roll (not daily mutate).
