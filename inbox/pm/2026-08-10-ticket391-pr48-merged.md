---
id: inbox-pm-ticket391-pr48-merged
agent: pm
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/48
---

# #391 PR #48 merged → Deploying Test

- PR https://github.com/yoosungung/nl2sql/pull/48 MERGED · merge_sha `9a891997c03506a73cad7047b7206f5be322360f` (head `c10b0bd`)
- CI green on merge head: backend / mcp-clippy / mcp-test / mcp (run 31354368667)
- Scope: describe `DESCRIBE_JSON_CHARS_MAX` budget (local022) + MCP error blocks semantic SQL scoring (local008) + success-path input SQL fallback for CI
- Next gate: tenant_cd test overlay + AC3 smoke `local008,local022` — empty SQL=0 · pass_rate>0
