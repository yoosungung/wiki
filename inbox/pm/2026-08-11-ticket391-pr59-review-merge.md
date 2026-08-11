---
id: inbox-pm-ticket391-pr59-review-merge
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/59
---

# #391 PR #59 Review merge → Deploying Test

- SoT 1870/1872: tip `test-6b63138` cleared overflow/timeout/infinity; residual empty-SQL=2 from bare MDL `decimal` dialect_unparse + prose/channel-thought stop without SSE sql.
- PR #59 merged `eb4bc95` (CI: backend/mcp-clippy/mcp-test/mcp green): MCP `arrow_type` bare decimal/numeric→Decimal128(38,10); `_to_sse` emits stash warehouse_sql before done on normal stream end.
- Post-merge board: Deploying Test / @ta tip roll `test-eb4bc95` + AC3 local008,local022 (empty SQL=0 · pass_rate>0). Done still needs test+qa+aa+prod.
