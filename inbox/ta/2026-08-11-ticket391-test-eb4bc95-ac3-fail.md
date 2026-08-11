---
id: inbox-ta-ticket391-test-eb4bc95-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/59
  - https://github.com/yoosungung/nl2sql/actions/runs/31460241537
  - https://github.com/yoosungung/nl2sql-releases/releases/tag/test-eb4bc95
---

# #391 AC3 fail on tip test-eb4bc95 (backend+MCP)

- Publish run 31460241537 **success** (backend+mcp-linux+publish-release). GHCR mcp image ImagePullBackOff → tip via releases binary `test-eb4bc95/nl2sql-mcp-linux-amd64` sha `ce8a4831…`.
- Backend `ghcr.io/yoosungung/nl2sql-backend:test-eb4bc95`; smoke health/ready 200.
- AC3 experiment `ticket391-agent-smoke-test-eb4bc95-20260811-055625` id `019fef64-c4e0-7e8e-87cf-cea84ea715db` → pass_rate **0.0**, empty SQL **2** (local008+local022 output `""`).
- MCP logs: no `dialect_unparse` this run (search_tables baseball OK) — decimal tip likely landed.
- Residual: analyst ToolMessage had `warehouse_sql` (ipl) but eval SSE extract empty; `BadRequest` `number is infinity when parsed as double` recurred mid-analyst.
