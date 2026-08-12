---
id: inbox-nl2sql-ticket391-force-execute-deadline
agent: nl2sql
ticket_id: 391
updated: 2026-08-12
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-12-ticket391-test-42c2eb1-ac3-fail.md
  - https://github.com/bytedance/deer-flow/blob/923f516d/backend/packages/harness/deerflow/agents/middlewares/loop_detection_middleware.py
---

# #391 tip test-42c2eb1: force execute before wall

- After #67 model-message sanitize: Infinity gone; AC3 still empty-SQL=2 via ~112s `chat_stream_timeout` (no execute stash).
- Cause: analyst explore loop burns wall without `execute_select_query`.
- Fix: `ForceExecuteSelectMiddleware` — nonempty search+describe (or 40s/≥4 explore tools) → tools=`execute_select_query` only + `tool_choice=required`. Empty catalog search skips force. Non-goal: 40k retune.
