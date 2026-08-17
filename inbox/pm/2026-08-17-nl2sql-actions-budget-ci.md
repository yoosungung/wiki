---
id: inbox-pm-nl2sql-actions-budget-ci
agent: pm
ticket_id: 920
updated: 2026-08-17
status: inbox
sources:
  - ticket:920
  - https://github.com/yoosungung/nl2sql/pull/108
  - https://github.com/yoosungung/nl2sql/actions/runs/31989380916
---

# nl2sql Actions budget blocks CI re-runs

- PR #108 tip `9df2308`: backend + mcp-clippy + mcp-test SUCCESS; required job id `mcp` aggregator failed ~3s with blank logs (known infra tip in ci.yml).
- Empty-commit retrigger `3dfe7e3` and workflow re-runs failed in ~2–3s with annotation: "The job was not started because an Actions budget is preventing further use."
- Branch protection API 404; `gh pr merge` succeeded while mergeStateStatus=UNSTABLE. Merge commit `c07d9c1`.
- Next: restore GH Actions minutes/budget; do not treat 2–3s all-job failures as product regressions when annotation cites Actions budget.
