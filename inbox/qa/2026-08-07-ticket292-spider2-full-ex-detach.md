---
id: inbox-qa-ticket292-spider2-full-ex-detach
agent: qa
ticket_id: 292
updated: 2026-08-07
status: inbox
sources:
  - ticket:292
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - spider2-eval/DESIGN.md
---

# #292 Spider2 local* Full EX detach heartbeat

- experiment=`ticket292-local-full-agent-ex-20260807-005059` Opik id=`019fd9b3-b33d-7cb9-91e8-2ee547675d64`
- pid=`19947` log=`/tmp/ticket292-full-ex-20260807-005059.log`
- progress ~67/135 (~50%, ~24s/it, ETA ~28m) — long-run detach; session health-check only
- gate: BadRequest/overflow/flood/Traceback/429 = 0; SGLang 40k/fp8 Ready
- pass_rate + failure summary = soft report after run completes → Review/@pm
