---
id: inbox-qa-ticket292-spider2-full-ex-result
agent: qa
ticket_id: 292
updated: 2026-08-07
status: inbox
sources:
  - ticket:292
  - spider2-eval/DESIGN.md
---

# Ticket 292 Spider2 local* Full EX result (soft)

- experiment=`ticket292-local-full-agent-ex-20260807-005059` id=`019fd9b3-b33d-7cb9-91e8-2ee547675d64`
- n=135 local* agent · wall≈01:19:28 · live SGLang `--context-length 40960`
- pass_rate(soft)=**0.0** · spider2_exec_match avg=0.0 · all 135 fail reason=`SQL execution failed: empty SQL` (agent eval output SQL empty; same soft pattern as #262 warehouse_sql null)
- Gate OK: BadRequest/context overflow/flood/429=0 · SQL-or-error+done termination observed during run
- Trace sample evaluation_task=`019fd9b3-b3b1-7b5a-8ac6-44ea91aecb6d` (local355) · LangGraph tags `nl2sql`/`deepagents` present on agent traces
- Non-blocking: pass_rate not a product gate pending Eric; report-only Full EX complete
