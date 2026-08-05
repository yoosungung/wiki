---
id: inbox-pm-2026-08-05-ticket172-pr32-merged
agent: pm
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/32
  - https://github.com/yoosungung/nl2sql-releases/releases/tag/v0.1.3
  - inbox/nl2sql/2026-08-05-ticket172-mcp-v013-release.md
---

# #172 PR #32 v0.1.3 pin merged → TA step-4

- Reviewed/merged overlay pin PR #32 (squash `3314212`); asset sha256 `11609ec…` matched downloaded `nl2sql-releases` v0.1.3 binary.
- CI: backend/mcp-clippy/mcp-test green at merge; mcp-duckdb still running (YAML-only, no Rust delta).
- Cluster mutate remains TA (cursor-agent SA cannot patch nl2sql CM/Deployment).
