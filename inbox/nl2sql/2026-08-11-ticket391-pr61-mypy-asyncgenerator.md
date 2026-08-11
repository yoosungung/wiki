---
id: inbox-nl2sql-ticket391-pr61-mypy-asyncgenerator
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - inbox/pm/2026-08-11-ticket391-pr61-mypy-bounce.md
  - https://github.com/yoosungung/nl2sql/pull/61
---

# #391 PR #61 mypy: AsyncGenerator for aclosing

- CI mypy: `aclosing(AsyncIterator)` type-var fail at chat.py:319.
- Fix tip `6b69575`: `run_agent_events` / `_to_sse` annotate `AsyncGenerator[dict, None]` (keeps asyncio.timeout + aclosing ContextVar-safe).
- Verify: `uv run --python 3.11 mypy src` Success · focused pytest 25 passed.
