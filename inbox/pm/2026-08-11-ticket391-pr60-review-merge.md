---
id: inbox-pm-ticket391-pr60-review-merge
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/60
---

# #391 PR #60 review→merge (SSE stash lifetime)

- SoT tip `test-eb4bc95`: ToolMessage had warehouse_sql but eval extract empty; infinity BadRequest recurred.
- PR #60: `reset_sse=False` until `_to_sse` + clear; warehouse-shaped ToolMessage emit; search/describe sanitize; CI green → merge `7363803`.
- Next: TA tip `test-7363803` + AC3 local008,local022.
