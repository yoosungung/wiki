---
id: inbox-pm-ticket391-pr53-review-merge
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/53
---

# #391 PR #53 review merge → Deploying Test

- PR #53 merged: merge_sha `117c0741f79ca9e98882277c0a3d470c9d5e2c52` (parent tip `3648949`).
- Scope: stash-first SSE sql · invent `baseball_players` gate (`looks_like_warehouse_sql`) · describe≤6k / search≤1k / ondemand≤1.5k / multi-turn≤11k.
- CI: backend · mcp-clippy · mcp-test · mcp all SUCCESS before merge.
- Next: TA tip roll `test-117c074` + AC3 `local008,local022` (empty SQL=0 · pass_rate>0). Done deferred until test+qa+aa+prod.
