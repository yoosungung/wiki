---
id: inbox-nl2sql-ticket391-timeout-path-eager-sql
agent: nl2sql
ticket_id: 391
updated: 2026-08-12
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-12-ticket391-test-732e959-ac3-fail.md
  - https://docs.python.org/3.11/library/asyncio-task.html
---

# #391 tip test-732e959: timeout-path empty SQL

- After #65 Infinity sanitize, AC3 still empty-SQL=2 via `chat_stream_timeout` (~90s wall).
- Nested `execute_select_query` may stash warehouse without parent `on_tool_end`; scoring only in TimeoutError handler races cleanup/eval.
- Fix: eager-emit scorable stash on each `_to_sse` event tick; wall default 90→110s (client 120s headroom). Non-goal: 40k retune.
