---
id: inbox-pm-nl2sql-920-tip-path-reopen
agent: pm
ticket_id: 920
updated: 2026-08-19
status: inbox
sources:
  - ticket:920
  - ticket:918
  - https://github.com/yoosungung/nl2sql/pull/108
---

# nl2sql #920 tip-path CD reopen

- Eric (#4160): registry option 2 tip-path; no product `deploy.yml`.
- Test (TA): Kaniko preferred; fallback `build-ghcr-images.yml` `tag=test-<short_sha>` + `tip_roll` backend → smoke.
- Prod: `prod.mode=package_manual` (nl2sql-releases / GHCR semver) — maintainer, not TA.
- Factory: agents.yaml tenant_cd + render-agents; ConfigMap roll then Deploying Test.
- pm: status Deploying Test · assignee ta · merge_sha `c07d9c1ac0054f6a1fe582d4dda9b29f540dafe0`; twin #918 after #920 test_*.
