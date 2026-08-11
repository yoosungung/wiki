---
id: inbox-nl2sql-ticket391-pr61-mcp-gate-flake
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/61
  - https://github.com/yoosungung/nl2sql/actions/runs/31467921936
---

# #391 PR #61 mcp aggregate gate flake

- CI: backend/mcp-clippy/mcp-test pass; required job `mcp` FAIL ~4s empty steps (log blob timeout / runnerless).
- `mcp` is needs-only echo gate — no product code path. Tip `9cf0eee` asserts needs results + timeout; prior empty retrigger `d1ab0b9`.
- Pod GH_TOKEN lacks actions:write — cannot `gh run rerun`; push tip re-queues CI.
