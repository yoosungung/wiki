---
id: inbox-ta-ticket391-test-7d78ec7-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - https://github.com/yoosungung/nl2sql/pull/55
  - https://github.com/yoosungung/nl2sql/actions/runs/31455463249
---

# #391 AC3 fail on test-7d78ec7 tip

- Test-Overlay: `publish-releases` run `31455463249` tag=`test-7d78ec7` (merge `7d78ec7` / PR #55) → live `ghcr.io/yoosungung/nl2sql-backend:test-7d78ec7`; annotations aligned; `/api/health`+`/api/ready` 200.
- AC3 experiment `ticket391-agent-smoke-test-7d78ec7-20260811-033314` id `019feee1-b119-7caf-b721-881626ba4569` → pass_rate **0.0**, spider2_exec_match **0** (2/2), duration ~5.5m.
- empty-SQL confirmed: local022 `output=""`; evaluation scored both instances 0 (Opik items stream incomplete for local008).
- Backend: StreamChunkTimeoutError (25s stall after chunks), TimeoutError/CancelledError; BadRequest `number is infinity when parsed as double` (SGLang JSON); EnsureAnalystTaskMiddleware did fill baseball empty `task({})` → analyst.
- Prior invent/overflow path from SoT 1829/1831 not the dominant failure on this tip — timeout/JSON BadRequest → no usable SSE sql.
