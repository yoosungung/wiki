---
id: inbox-pm-ticket391-pr61-ci-bounce
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/61
---

# #391 PR #61 CI bounce (ContextVar + wait_for)

- Scope OK vs SoT 1895 (channel-call promote, terminate_on_close=False, wall timeout).
- CI backend FAIL on py3.11: `test_chat_emits_sql_from_deepagents_command_shape` — `_to_sse` `asyncio.wait_for(aiter.__anext__)` → `run_agent_events` finally `reset_request_context` raises `ValueError: Token was created in a different Context`.
- py3.12 local full suite can pass; reproduce with `uv sync --extra dev --locked --python 3.11 && uv run pytest`.
- Do not merge until CI green.
