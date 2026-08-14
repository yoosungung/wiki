---
id: inbox-nl2sql-ticket770-local228-missing-relation
agent: nl2sql
ticket_id: 770
updated: 2026-08-14
status: inbox
sources:
  - ticket:770
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Semantic-View-Single-Master.md
---

# local228: ipl_match_event is not a Postgres relation

- Scoreboard `relation "ipl_match_event" does not exist` means the MDL model name leaked into warehouse SQL. Physical FROM is `ipl.ball_by_ball` (+ JOIN `ipl.match` for season_id).
- Prefer seal `ipl_season_top3_bat_bowl` for per-season top-3 bat/bowl. Do not copy #769 career `kind_out` onto that seal.
- Catalog regression: `mcp/tests/search_ipl_sql_exec_catalog.rs` needles `not a postgres relation` + rank seal before `ipl_match_event`.
