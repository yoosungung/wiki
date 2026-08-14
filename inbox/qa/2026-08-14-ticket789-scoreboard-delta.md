---
id: inbox-qa-ticket789-scoreboard-delta
agent: qa
ticket_id: 789
updated: 2026-08-14
status: inbox
sources:
  - ticket:789
  - ticket:779
  - ticket:781
  - ticket:782
  - ticket:783
  - ticket:784
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - spider2-eval/DESIGN.md
---

# Scoreboard delta Full EX (#789)

- After #781/#782/#783/#784 merge (tip `8048c28e`), Full EX pass_rate **0.3259** (44/135), delta **+10** vs #779 0.2519. Not weekly canary.
- Wins: local021, local065, local098 now PASS. local073 sql_exec→mismatch (still fail). PG conn-closed **0**.
- Residual: IPL local258/025/023/020 mismatch; modern_data local073/066/049/040; db-imdb local100/096 mismatch; city_legislation sql_exec regression n=5.
- CLI `scoreboard-*.json` still omits `instance_id`; rebuild from Opik `experiment.get_items()`.
- Live metadata PVC SHA ≠ product git SHA; scoreboard measures tip live chat SSE.
