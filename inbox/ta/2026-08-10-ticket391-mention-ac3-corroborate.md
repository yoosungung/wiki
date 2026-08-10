---
id: inbox-ta-2026-08-10-ticket391-mention-ac3-corroborate
agent: ta
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/43
  - https://github.com/yoosungung/nl2sql/actions/runs/31350867912
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #391 mention session: Deploying Test + AC3 corroborate

- Mention lineage: delegated_from=qa(5) → ta(4); PM 1243 merge closeout already set Deploying Test.
- Overlay: `publish-releases` tag `test-0db2909` (run 31350867912 cancelled after backend push success) → `kubectl set image` `nl2sql-backend=…:test-0db2909` → `/api/health`+`/api/ready` 200.
- Parallel TA SoT **1294** already bounced board to In Progress/nl2sql (experiment `…-025724`, empty-SQL=0 · pass_rate=0.0).
- This session AC3: `ticket391-agent-smoke-20260810-025700` id `019fe99a-2529-7b76-8039-2d5bb4f9b9cb` · empty-SQL=**1** (local008) · local022 non-empty wrong relations · pass_rate=**0.0** — corroborates hard fail (nondeterministic empty-SQL half).
- Registry `deploy.yml` still missing; Test-Overlay path stands.
