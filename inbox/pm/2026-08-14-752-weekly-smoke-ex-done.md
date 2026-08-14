---
id: inbox-pm-752-weekly-smoke-ex-done
agent: pm
ticket_id: 752
updated: 2026-08-14
status: inbox
sources:
  - ticket:752
  - https://github.com/yoosungung/nl2sql/pull/91
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
---

# #752 weekly-smoke agent EX sealed

- Tip already served `baseball_highest_games_runs_hits_hr` + `ipl_scored_100_runs_lost_match`; metadata git SHA need not equal product `merge_sha` when those models are present.
- `spider2-opik run --task agent --instance-ids local008,local022` pass_rate 1.0 → NF Done. Not tenant_cd / Deploying Test.
