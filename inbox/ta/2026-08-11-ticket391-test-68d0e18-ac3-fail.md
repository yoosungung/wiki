---
id: inbox-ta-ticket391-test-68d0e18-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - https://github.com/yoosungung/nl2sql/pull/56
  - https://github.com/yoosungung/nl2sql/actions/runs/31456826962
---

# #391 AC3 fail on test-68d0e18 tip

- Test-Overlay: `publish-releases` run `31456826962` tag=`test-68d0e18` (merge `68d0e18` / PR #56) → live `ghcr.io/yoosungung/nl2sql-backend:test-68d0e18`; annotations aligned; `/api/health`+`/api/ready` 200.
- AC3 experiment `ticket391-agent-smoke-test-68d0e18-20260811-035718` id `019feef7-b9c4-7ae6-9dd2-0aa7967321bf` → pass_rate **0.0**, spider2_exec_match **0** (2/2), duration ~9.5m.
- empty-SQL: local008 `output=""` confirmed; evaluation scored both instances 0.
- PR #56 effect: StreamChunkTimeout / infinity-JSON BadRequest **0** in window (addressed).
- Remaining blocker: BadRequest context overflow `42588>40960` and `42489>40960` (input ~40.5k + completion 2048) during analyst/task → no usable SSE sql.
