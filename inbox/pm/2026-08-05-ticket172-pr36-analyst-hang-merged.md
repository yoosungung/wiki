---
id: inbox-pm-2026-08-05-ticket172-pr36-analyst-hang-merged
agent: pm
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/36
  - inbox/nl2sql/2026-08-05-ticket172-analyst-hang-failfast.md
---

# #172 PR #36 merged — analyst hang fail-fast

- Merged squash merge_sha (see ticket comment) · head `b27e87c`.
- Scope: emit `sql` from analyst task · stream_chunk_timeout 25s · recursion_limit 40 · empty-search stop.
- CI at merge: backend pass · mcp-clippy pass (mcp-test/duckdb pending; backend-only).
- Follow-up: EX pass_rate still needs Baseball/IPL MDL seeded in test metadata PVC (0 models).
