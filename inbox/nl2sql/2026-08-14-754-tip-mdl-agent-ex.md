---
id: inbox-nl2sql-754-tip-mdl-agent-ex
agent: nl2sql
ticket_id: 754
updated: 2026-08-14
status: inbox
sources:
  - ticket:754
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - https://github.com/yoosungung/nl2sql/pull/93
---

# #754 tip MDL roll + agent EX (local259 / local228)

- Product merge SHA is not MCP search SHA. After PR #93, PUT IPL seals on tip metadata git; MCP `/admin/sync` `status=ok` at `5e6b097be5afdeb04764dcf7c8ae8f89f0bd57f9`.
- Agent EX: `SPIDER2_AGENT_BASE_URL=http://nl2sql-backend.nl2sql.svc.cluster.local:8080` + `SPIDER2_AGENT_AUTH_*` → `spider2-opik run --task agent --instance-ids local259,local228 --experiment-name 754-local259-local228-tip-mdl`.
- local228: `spider2_exec_match=1.0` via `ipl_season_top3_bat_bowl` refSql; no `e.__rel_event__season_id`.
- local259: SQL exec succeeded (reason `result mismatch`, not `SQL execution failed`); pred used `ipl_player_career_stats` and did not invent warehouse `br`. Residual is gold-vs-pred career aggregates, not sql_exec_failed.
