---
id: inbox-ta-nl2sql-918-tip-kaniko
agent: ta
ticket_id: 918
updated: 2026-08-19
status: inbox
sources:
  - ticket:918
  - ticket:920
  - https://github.com/yoosungung/nl2sql/pull/107
---

# nl2sql #918 tip Kaniko Deploying Test

- Tip tag `test-<short_sha>` from merge_sha; Kaniko git-clone needs **branch** ref (`main`), not raw commit SHA — SHA as `--branch` fails Init:Error.
- tip_roll: set container name `backend` (not deployment name) on `nl2sql-backend`.
- Smoke FQDN may briefly fail during terminating old pod; retry ClusterIP/podIP → HTTP 200.
- prod.mode=package_manual — no TA Deploying Prod; hand QA/AA then PM Done.
