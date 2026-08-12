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
  - inbox/ta/2026-08-12-nl2sql-kaniko-tip-path.md
---

# #391 AC3 fail on tip test-ef665d6

- Tip live via #551 Kaniko (`test-ef665d6` / merge `ef665d6`); smoke `/api/health`+`/api/ready` 200.
- AC3 experiment `ticket391-agent-smoke-test-ef665d6-20260812-040800` id `019ff427-e404-7d70-b366-f20af0af3d4e` — ~90s (no hang) · empty SQL **2** · pass_rate **0**.
- Backend during run: SGLang `BadRequest` (`number is infinity when parsed as double`) then `TimeoutError` from `chat_stream_timeout`; eval extract still empty.
- Force-analyst (#64) did not clear AC3 empty-SQL gate on local008/local022.
