---
id: inbox-nl2sql-ticket391-model-message-sanitize
agent: nl2sql
ticket_id: 391
updated: 2026-08-12
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-12-ticket391-test-754707c-ac3-fail.md
  - https://github.com/sgl-project/sglang/issues/4097
---

# #391 tip test-754707c: model-bound Infinity sanitize

- After #66 (eager SQL emit + 110s wall): AC3 still empty-SQL=2 · ~110s timeout ×2 · Infinity BadRequest resurfaced once.
- Gap: tool-output middleware alone left non-finite values in message history / tool_call args (and numpy-like scalars) on the next chat completion.
- Fix: `sanitize_message_for_llm` + `SanitizeNonFiniteToolMiddleware.wrap_model_call` override messages before LLM. Non-goal: 40k retune.
