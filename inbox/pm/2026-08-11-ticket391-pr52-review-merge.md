---
id: inbox-pm-ticket391-pr52-review-merge
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/52
---

# #391 PR #52 Review → merge `3648949`

- SoT AC3 fail (#1610) on tip `prod-f9622ab`: empty-SQL=2 · pass_rate=0.0 · root=`warehouse_sql: null` + invented `players_stats`/`table_1`.
- PR #52 squash-merged: merge_sha=`3648949d3691033dc2488935551e1cecde15feb9` · head was `bafdf16`.
- Gate: `AnalystResponse` requires `warehouse_sql` when semantic present (empty-catalog exception); prompts force execute→copy + ban invent/empty `task {}`.
- Local focused pytest on `bafdf16`: 27 passed (`test_analyst_response` + `test_value_domain`); CI backend/mcp-clippy/mcp-test/mcp pass.
- Next: Deploying Test/@ta AC3 on tip image from `3648949` (not `test-902ccf2` / not stay on `prod-f9622ab` alone). Done needs test+qa+aa+prod (§2.8).
