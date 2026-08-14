---
id: inbox-nl2sql-ticket769-local259-career-wickets
agent: nl2sql
ticket_id: 769
updated: 2026-08-14
status: inbox
sources:
  - ticket:769
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - https://github.com/yoosungung/nl2sql/pull/94
---

# local259 career EX: hit wicket counts; CAST numeric for Opik

- After sql_exec seal, local259 mismatch vs gold_c was bowling only (Sreesanth best `2-8` vs `3-28`).
- Gold credits `hit wicket` to the bowler; exclude `run out`, `retired hurt`, `obstructing the field`. Do not copy that list onto `ipl_season_top3_bat_bowl` (local228 already matched).
- Opik `compare_pandas_table` only `isclose`s Python int/float. Postgres `numeric` → Decimal fails the gold int64/float64 vectors; CAST refSql aggregates to `bigint`/`double precision`.
