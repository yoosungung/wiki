---
id: inbox-ta-ticket391-test-6572a7b-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - https://github.com/yoosungung/nl2sql/pull/54
  - https://github.com/yoosungung/nl2sql/actions/runs/31453924169
---

# #391 AC3 fail on test-6572a7b tip

- Test-Overlay: `publish-releases` run `31453924169` tag=`test-6572a7b` (merge `6572a7b` / PR #54) → live `ghcr.io/yoosungung/nl2sql-backend:test-6572a7b`; annotations image-tag/merge-sha aligned; `/api/health`+`/api/ready` 200.
- AC3 experiment `ticket391-agent-smoke-test-6572a7b-20260811-030201` id `019feec5-1d0c-7209-a83c-c4ac69312da1` → pass_rate **0.0**, spider2_exec_match **0**, duration ~9m.
- empty-SQL=**2**: local008+local022 both `output=""` · reason `SQL execution failed: empty SQL`.
- Backend window: BadRequest context overflow `42902 > 40960` (input 40854 + completion 2048) during analyst/task path; also StreamChunkTimeoutError / TimeoutError — no usable SSE `sql` emitted.
- Prior SoT empty `task({})` on `test-117c074` may be mitigated by #54 middleware, but tip still fails AC3 via overflow/timeout → empty SQL.
