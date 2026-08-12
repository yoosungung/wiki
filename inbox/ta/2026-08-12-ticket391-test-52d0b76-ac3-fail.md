---
id: inbox-ta-ticket391-test-52d0b76-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-12
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/61
  - https://github.com/yoosungung/nl2sql/pull/63
---

# #391 AC3 fail on tip test-52d0b76

- Tip live via #551 Kaniko (`test-52d0b76`); smoke ready 200. Includes main after #61 SSE wall timeout.
- AC3 experiment `ticket391-agent-smoke-test-52d0b76-20260812-034608` id `019ff413-dad1-73dd-a158-d1085dc3dd92` — completed ~91s (no hang) · empty SQL **2** · pass_rate **0**.
- Residual: model empty `finish_reason=stop` / no tool_calls; backend `TimeoutError` from `chat_stream_timeout`; eval extract still empty.
- SSE hang SoT 1895 mitigated by wall timeout; empty-SQL product gate still open.
