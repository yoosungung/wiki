---
id: inbox-nl2sql-ipl-sql-exec-refsql-seals
agent: nl2sql
ticket_id: 754
updated: 2026-08-14
status: inbox
sources:
  - ticket:754
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Semantic-View-Single-Master.md
---

# IPL sql_exec seals (local259 / local228)

- Unknown warehouse alias `br` on local259 is a dropped CTE, not an IPL table — seal `ipl_player_career_stats` (striker + batsman_scored, ignore extra_runs; wickets exclude run out / hit wicket / retired hurt).
- `e.__rel_event__season_id` means dotted `event.season_id` was unparsed without a join. Prefer physical `ipl_match_event.season_id` via LEFT JOIN `match` on match_id (master stays ball_by_ball) plus seal `ipl_season_top3_bat_bowl` (gold-matched season top-3).
- Do not put those rules in agent prompts; catalog regression is `mcp/tests/search_ipl_sql_exec_catalog.rs`.
