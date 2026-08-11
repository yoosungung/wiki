---
id: inbox-nl2sql-ticket391-channel-call-sse-wall
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md
  - https://github.com/yoosungung/nl2sql/pull/61
---

# #391 tip test-7363803: channel-call + SSE wall clock

- Live hang: POST /api/chat 0 SSE events · backend `Session termination failed: 202` · gemma `<|channel>call:task…` without native tool_calls.
- Fix: parse/promote channel prose in EnsureAnalystTaskMiddleware; MCP `terminate_on_close=False`; `_to_sse` wall `NL2SQL_CHAT_STREAM_TIMEOUT_S` default 90s → error+done (wiki fail-fast: 침묵 hang 금지).
- Non-goal: SGLang 40k retune. AC3 still needs tip roll after merge.
