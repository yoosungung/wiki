---
id: inbox-qa-nl2sql-1003-scoreboard-outcome
agent: qa
ticket_id: 1003
updated: 2026-08-20
status: inbox
sources:
  - ticket:1003
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# nl2sql #1003 Full EX scoreboard outcome

- Experiment `scoreboard-agent-20260819T092611Z`: pass_rate **0.3407** (46/135); baseline #789 0.3259 (44/135); delta **+0.0148** (+2).
- CLI report may lack `instance_id`/mis-classify until rebuilt via Opik `experiment.get_items()` (wiki §7.3).
- Top residual clusters (metadata): empty_sql×10; bank_sales_trading sql_exec×4; f1 sql_exec×2; bank mismatch×7; city_legislation mismatch×5.
