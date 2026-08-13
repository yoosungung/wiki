---
id: inbox-qa-nl2sql-qa-bulk-weekly-agent-smoke
agent: qa
ticket_id: 683
updated: 2026-08-13
status: inbox
sources:
  - ticket:683
  - ticket:685
  - wiki/Agents/Text-to-SQL/000_Text-to-SQL-MOC.md
---

# nl2sql qa-bulk-weekly agent smoke = 0

- Manual fire #683 @ nl2sql `7f519f2`: `spider2-opik weekly` — gold-sql `weekly-gold-sql-smoke` pass_rate 1.0; agent `weekly-agent-smoke` pass_rate 0.0 (local008 Baseball, local022 IPL).
- Process exit stayed 0: `cli.run` always returns 0; #391 "agent hard" only propagates subprocess nonzero, not pass_rate floor.
- Detach tip: plain `nohup` under Cursor shell can die mid-agent; `setsid` + exit file is more reliable for long_run.
- Failure filed as New #685 for PM→IC.
