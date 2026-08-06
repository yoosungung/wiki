---
id: inbox-qa-ticket262-agent-smoke-32k
agent: qa
ticket_id: 262
updated: 2026-08-06
status: inbox
sources:
  - ticket:262
  - ticket:261
  - ticket:172
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - inbox/ta/2026-08-06-sglang-gemma4-12b-context-32k.md
---

# Agent smoke after SGLang 32K (#262)

- Experiment `ticket262-agent-smoke-32k-20260806-075537` on Opik project `nl2sql`: pass_rate **0.0** (local008/local022 empty SQL).
- 16K BadRequest gone in smoke window; agent can still hit **32K** overflow (≈31.5k input + 2k completion reserve).
- Chat path ends `analyst_no_sql` + `done` when no warehouse SQL emitted.
- Test backend lacks `OPIK_URL_OVERRIDE` → LangGraph `OpikTracer` off; only evaluate-runner `evaluation_task` traces appear.
