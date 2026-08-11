---
id: inbox-nl2sql-ticket391-pr54-mypy-fix
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - inbox/pm/2026-08-11-ticket391-pr54-mypy-bounce.md
  - https://github.com/yoosungung/nl2sql/pull/54
---

# #391 PR #54 mypy ToolCall typing fix

- Bounce: `task_guard.py` list[dict] vs list[ToolCall].
- Fix: build/assign via `ToolCall(...)` TypedDict; `mypy src` clean; test_task_guard 9 passed.
