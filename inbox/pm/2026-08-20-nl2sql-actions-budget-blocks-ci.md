---
id: inbox-pm-nl2sql-actions-budget-blocks-ci
agent: pm
ticket_id: 1051
updated: 2026-08-20
status: inbox
sources:
  - ticket:1051
  - https://github.com/yoosungung/nl2sql/pull/110
  - https://github.com/yoosungung/nl2sql/actions/runs/32321100206
---

# nl2sql CI Actions budget blocks merge

- PR jobs fail in ~3s with empty steps / `runner_id=0` when annotation is: "The job was not started because an Actions budget is preventing further use."
- Sibling open PRs (#109/#110) hit the same failure — not content regressions.
- PM policy: do not merge on red CI without Eric grant; escalate Actions budget or merge-without-CI exception; metadata-only tickets stay tenant_cd N/A (no TA Deploying Test).
