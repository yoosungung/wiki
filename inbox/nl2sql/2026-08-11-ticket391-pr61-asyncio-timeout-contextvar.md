---
id: inbox-nl2sql-ticket391-pr61-asyncio-timeout-contextvar
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - inbox/pm/2026-08-11-ticket391-pr61-ci-bounce.md
  - https://github.com/yoosungung/nl2sql/pull/61
  - https://github.com/python/cpython/issues/102123
---

# #391 PR #61 CI: wait_for → asyncio.timeout

- py3.11 CI fail: `asyncio.wait_for(aiter.__anext__)` → new Task → `reset_request_context` ValueError (ContextVar token mismatch).
- Fix: `_to_sse` uses `asyncio.timeout` + `contextlib.aclosing` (same Context). Tip `7c37ee7`.
- Repro: `uv sync --extra dev --locked --python 3.11 && uv run pytest tests/test_chat.py::test_chat_emits_sql_from_deepagents_command_shape`.
