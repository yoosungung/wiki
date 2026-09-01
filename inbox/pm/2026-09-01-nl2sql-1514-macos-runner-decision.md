---
id: inbox-pm-nl2sql-1514-macos-runner-decision
agent: pm
ticket_id: 1514
updated: 2026-09-01
status: inbox
sources:
  - ticket:1514
  - https://github.com/yoosungung/nl2sql/actions/runs/33381902133
---

# #1514 publish-releases macOS runner gate

- `publish-releases` run 33381902133: meta/verify-ghcr success; `build-mcp-macos` still queued (self-hosted macOS offline).
- `nl2sql-releases` tag v0.1.4 absent until macos asset job runs.
- Human gate: keep self-hosted wait vs approve `macos-latest` (cost/infra) — PM recommends (2) unless self-hosted ETA ≤~2h.
