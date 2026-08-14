---
id: inbox-qa-ticket767-scoreboard-delta
agent: qa
ticket_id: 767
updated: 2026-08-14
status: inbox
sources:
  - ticket:767
  - ticket:751
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - spider2-eval/DESIGN.md
---

# Scoreboard delta Full EX (#767)

- After #752/#753/#754 merge, Full EX pass_rate stayed **0.2222** (30/135) with swap +16/−16. Not weekly canary.
- Wins: `local022` and `local065` now PASS. `local259` sql_exec → result_mismatch.
- `local008` sql_exec was PG `server closed the connection` (sql emitted); 12/28 sql_exec are that flake — do not treat as MDL miss.
- CLI `scoreboard-*.json` still omits `instance_id`; rebuild from Opik `experiment.get_items()`.
- Live metadata PVC SHA ≠ product git SHA; scoreboard measures tip live chat SSE.
