---
id: inbox-nl2sql-ticket391-infinity-sanitize-middleware
agent: nl2sql
ticket_id: 391
updated: 2026-08-12
status: inbox
sources:
  - ticket:391
  - https://github.com/sgl-project/sglang/issues/4097
  - https://github.com/openai/openai-agents-python/pull/3657
---

# #391 tip test-ef665d6: Infinity sanitize hardening

- Residual after force-analyst (#64): SGLang BadRequest `number is infinity when parsed as double` → chat_stream_timeout → empty SQL.
- Gap: `slim_execute_for_llm` sanitized rows only; columns/error dicts and ToolMessage Python `Infinity` tokens still reached chat completions.
- Fix: `sanitize_json_numbers` covers `numbers.Real`; `sanitize_tool_output` rewrites ToolMessage/Command; `SanitizeNonFiniteToolMiddleware` on orchestrator+analyst; execute error path sanitized.
- Non-goal: do not retune `max_model_len=40960`.
