---
id: inbox-nl2sql-ticket793-local258-bowler-seal
agent: nl2sql
ticket_id: 793
updated: 2026-08-14
status: inbox
sources:
  - ticket:793
  - ticket:782
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
---

# local258 bowler card: legal balls exclude wides/noballs; include 0-wicket

- Gold (329 rows) is per-bowler wickets / economy / **bowling** SR / best `wickets-runs`. Economy = 6 * bat runs / legal balls; SR = legal balls / wickets. Legal balls = not `extra_runs` wides/noballs. Include 0-wicket bowlers.
- `ipl_player_career_stats.strike_rate` is batting SR and uses batsman_scored ball counts — do not reuse that grain. kind_out exclude run out / retired hurt / obstructing the field (hit wicket counts; do not copy local228).
- Seal `ipl_bowler_wickets_economy_strike_best`. Catalog: `mcp/tests/search_ipl_bowler_career_catalog.rs`.
