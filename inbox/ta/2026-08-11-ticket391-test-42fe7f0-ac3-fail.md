---
id: inbox-ta-ticket391-test-42fe7f0-ac3-fail
agent: ta
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - https://github.com/yoosungung/nl2sql/pull/57
  - https://github.com/yoosungung/nl2sql/actions/runs/31458182054
---

# #391 AC3 fail on test-42fe7f0 tip

- Test-Overlay: `publish-releases` run `31458182054` tag=`test-42fe7f0` (merge `42fe7f0` / PR #57) → live `ghcr.io/yoosungung/nl2sql-backend:test-42fe7f0`; annotations aligned; health/ready 200.
- AC3 experiment `ticket391-agent-smoke-test-42fe7f0-20260811-042359` id `019fef10-2801-7d67-bdbf-6022cc7d60eb` → pass_rate **0.0**, spider2_exec_match **0** (2/2), duration ~4.9m.
- empty-SQL: local008 `output=""` confirmed.
- PR #57 effect: StreamChunkTimeout/infinity still **0**; max_tokens=1024 visible in overflow math (`40009+1024`).
- Remaining blocker: context overflow — input alone `59320>40960` and `41033>40960` (input 40009 + completion 1024) → no usable SSE sql. Tool/history trimming still insufficient under multi-turn.
