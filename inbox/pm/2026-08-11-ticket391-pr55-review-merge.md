---
id: inbox-pm-ticket391-pr55-review-merge
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/55
---

# #391 PR #55 review merge → Deploying Test

- PR #55 merged: merge_sha `7d78ec7dad1fcd96d7a0a1d2fd97e003ac2ac39e` (parent tip `6572a7b`).
- Scope: MCP warehouse-only SSE scoring (reject MDL invent) · stash warehouse_sql only · budgets describe≤5.5k/search≤800/ondemand≤1.2k/multi-turn≤10k.
- Addresses SoT 1829 invent/incomplete FROM + SoT 1831 overflow path.
- CI: backend · mcp-clippy · mcp-test · mcp SUCCESS.
- Next: TA tip roll `test-7d78ec7` + AC3 local008,local022 (empty SQL=0 · pass_rate>0).
