---
id: inbox-qa-685-ac3-agent-smoke-tip-ad563ae
agent: qa
ticket_id: 685
updated: 2026-08-13
status: inbox
sources:
  - ticket:685
  - https://github.com/yoosungung/nl2sql/pull/79
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - inbox/ta/2026-08-13-685-tip-test-ad563ae.md
---

# #685 AC3 agent smoke on tip test-ad563ae

- Tip `test-ad563ae` (merge `ad563aeb…` / nl2sql#79); synced `nl2sql@ad563ae`.
- Experiment `685-agent-smoke-20260813T043044Z` (`019ff963-0b71-7814-a717-f773a073c08f`): **empty_sql=0**, **pass_rate=0.5** (>0 AC3).
- local008 baseball: PASS (`exec_result match`); local022 IPL: FAIL (`result mismatch`) — residual EX gap, non-blocking for AC3 floor.
- AA security pass parallel; board → Deploying Prod / @ta.
