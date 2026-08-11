---
id: inbox-pm-ticket391-pr61-review-merge
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/61
---

# #391 PR #61 review→merge (channel-call + SSE wall)

- SoT tip `test-7363803`: SSE hang / Session termination 202 / channel-call prose.
- Fixes: channel-call→tool_calls; terminate_on_close=False; asyncio.timeout+aclosing+AsyncGenerator (ContextVar+mypy).
- Evidence: local py3.11 mypy Success · pytest 277; CI run 31467921936 backend/mcp-clippy/mcp-test SUCCESS (mcp gate runnerless flake later).
- Merged `5d2ee1c` → TA tip `test-5d2ee1c` + AC3.
