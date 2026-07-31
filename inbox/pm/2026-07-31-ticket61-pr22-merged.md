---
id: inbox-pm-ticket61-pr22-merged
agent: pm
ticket_id: 61
updated: 2026-07-31
status: inbox
sources:
  - ticket:61
  - https://github.com/yoosungung/nl2sql/pull/22
---

# #61 @pm mention — PR22 AA remediation merge

- Reviewed PR #22: Secret-only `MCP_SHARED_TOKEN` (secretRef), remove `NL2SQL_DEV_*`, mcp sha256 pin, verify-deploy-docs gates.
- Merged squash → `b51041cc893b2cb34898226c2611418b5e16c292` (CI: backend/mcp-clippy SUCCESS; mcp-test/duckdb still running — deploy-only).
- Hand off → QA/@aa recheck (live remédiation already claimed by ta). tenant_cd: N/A.
