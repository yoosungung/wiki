---
id: inbox-ta-ticket391-test-ef665d6-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-12
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/64
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #391 AC3 fail on tip test-ef665d6

- Tip live via #551 Kaniko (`test-ef665d6` = PR #64 merge `ef665d6`); smoke `/api/health`+`/api/ready` HTTP 200.
- AC3 experiment `ticket391-agent-smoke-test-ef665d6-20260812-040951` id `019ff429-9d50-7204-af61-312126bb676e` — ~91s (no hang) · empty SQL **2** · pass_rate **0**.
- Trace sample local022: output empty · reason `SQL execution failed: empty SQL` · trace `019ff429-9d92-74b6-9173-1e629602e896`.
- Live logs during run: `chat_stream_timeout` TimeoutError · residual `BadRequest number is infinity` · `EnsureAnalystTaskMiddleware.after_model: None` — force-analyst tip did not clear empty-SQL gate.
