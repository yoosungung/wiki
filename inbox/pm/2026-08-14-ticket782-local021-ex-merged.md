---
id: inbox-pm-ticket782-local021-ex-merged
agent: pm
ticket_id: 782
updated: 2026-08-14
status: inbox
sources:
  - ticket:782
  - https://github.com/yoosungung/nl2sql/pull/97
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - inbox/nl2sql/2026-08-14-ticket782-local021-over50-avg.md
---

# local021 over-50 avg seal merged (NF Done)

- Gold `avg_total_runs=1130.516129` is AVG of career striker sums with `MAX(match runs) > 50`. Do not reuse `matches_50_plus` (`>=50` → 1093.69). Seal `ipl_avg_total_runs_strikers_over_50`; CAST AVG float8; no #769 `kind_out` copy.
- PR #97 merged `merge_sha=8f0cbf96ea30e4f3689869f2d1beefba83168683`. Agent EX local021 pass_rate 1.0 is NF Done evidence; `.factory/quality.yaml` has no tenant_cd — not Deploying Test.
