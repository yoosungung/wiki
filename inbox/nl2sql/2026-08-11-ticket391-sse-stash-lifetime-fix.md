---
id: inbox-nl2sql-ticket391-sse-stash-lifetime-fix
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-11-ticket391-test-eb4bc95-ac3-fail.md
---

# #391 tip test-eb4bc95 — SSE stash lifetime + infinity

- SoT: ToolMessage had warehouse_sql but extract_last_sql empty; infinity BadRequest recurred mid-analyst.
- Root: `run_agent_events` finally reset execute SSE ContextVar before `_to_sse` post-loop stash emit.
- Fix: `reset_sse=False` until `_to_sse` clears; emit warehouse-shaped ToolMessage sql without stash; sanitize search/describe/ondemand floats.
- Verify: related pytest 51 passed.
