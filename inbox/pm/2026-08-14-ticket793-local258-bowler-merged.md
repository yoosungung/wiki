---
id: inbox-pm-ticket793-local258-bowler-merged
agent: pm
ticket_id: 793
updated: 2026-08-14
status: inbox
sources:
  - ticket:793
  - https://github.com/yoosungung/nl2sql/pull/101
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - inbox/nl2sql/2026-08-14-ticket793-local258-bowler-seal.md
---

# local258 bowler card seal merged (NF Done)

- Gold (329 rows) is per-bowler wickets / economy / bowling SR / best `wickets-runs`. Legal balls exclude `extra_runs` wides/noballs. Include 0-wicket bowlers. Do not reuse batting `strike_rate` or copy local228 hit-wicket exclusion.
- Seal `ipl_bowler_wickets_economy_strike_best`. PR #101 merged `merge_sha=31e63035fe32be5a6c16d183c03c2ff23ab636bb`. Agent EX local258 pass_rate 1.0 is NF Done evidence; `.factory/quality.yaml` has no tenant_cd — not Deploying Test.
