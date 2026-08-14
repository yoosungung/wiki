---
id: inbox-pm-ticket769-local259-ex-merged
agent: pm
ticket_id: 769
updated: 2026-08-14
status: inbox
sources:
  - ticket:769
  - https://github.com/yoosungung/nl2sql/pull/94
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - https://en.wikipedia.org/wiki/Hit_wicket
---

# local259 career EX: hit wicket credits bowler

- IPL gold_c bowling credits `hit wicket` to the bowler; exclude `run out` / `retired hurt` / `obstructing the field`. Do not copy that list onto `ipl_season_top3_bat_bowl` (local228 already matched).
- Opik `compare_pandas_table` `isclose`s only Python int/float. CAST refSql aggregates to `bigint`/`double precision` or Postgres `numeric` → Decimal fails gold vectors.
- Agent EX `local259,local021` pass_rate 1.0 after tip PUT of `ipl_player_career_stats` is NF Done evidence; not tenant_cd / Deploying Test.
