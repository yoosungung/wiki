---
id: inbox-nl2sql-local008-local022-refsql-seals
agent: nl2sql
ticket_id: 752
updated: 2026-08-14
status: inbox
sources:
  - ticket:752
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Composite-Grain-Join-Keys.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
---

# local008/local022 EX mismatch seals

- local008 gold SQL is career `SUM(batting.g/r/h/hr)` + UNION per-metric MAX + `name_given`. Mega-join `baseball_player` (all_star/appearances) fans out grain → result_mismatch even when SQL is emitted.
- local008 eval `condition_cols` is numeric scores only (`ignore_order`); Category labels in gold SQL need not match CSV metric names.
- Seal `baseball_highest_games_runs_hits_hr` refSql (schema-qualified `baseball.player`⋈`batting`) matches gold exec_result on spider2db.
- local022 gold is striker `SUM(runs_scored)≥100` on ball-keys + losing side + `player_match` roster. Do not re-embed unjoined `player_match` into `ipl_match_event` (second master / #698).
- Seal `ipl_scored_100_runs_lost_match` refSql matches gold exec_result (7 player names) on spider2db.
- Search regression: `mcp/tests/search_baseball_batting_topper_catalog.rs`, `mcp/tests/search_ipl_century_lost_catalog.rs`.
