---
id: inbox-nl2sql-ticket782-local021-over50-avg
agent: nl2sql
ticket_id: 782
updated: 2026-08-14
status: inbox
sources:
  - ticket:782
  - ticket:769
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
---

# local021 over-50 avg is career SUM then AVG, threshold >50

- Gold `avg_total_runs=1130.516129` is AVG of career striker sums for players with MAX(per-match runs) **> 50**. `ipl_player_career_stats.matches_50_plus` is **>=50** and yields 1093.69 — do not reuse that grain.
- Seal `ipl_avg_total_runs_strikers_over_50` (ball_by_ball⋈batsman_scored composite keys; CAST AVG to float8). Do not copy #769 `kind_out` onto this batting-only model. Catalog: `mcp/tests/search_ipl_over50_avg_catalog.rs`.
