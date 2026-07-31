---
id: inbox-ta-nl2sql-test-prod-deploy-paths
agent: ta
ticket_id: 59
updated: 2026-07-31
status: inbox
sources:
  - ticket:59
  - https://github.com/yoosungung/nl2sql/pull/20
  - https://github.com/yoosungung/nl2sql-releases
---

# nl2sql Test vs Prod deploy paths

- Test = k8s namespace `nl2sql` via `deploy/k8s/base` + `deploy/SETUP.md`; overlays not present yet (ROADMAP Phase 4).
- Prod package = `.github/workflows/publish-releases.yml` → `nl2sql-releases` Release assets + GHCR (not a runtime deploy into the releases repo).
- Doc smoke: `./deploy/scripts/verify-deploy-docs.sh` (markers + kubectl client dry-run).
- Shared cluster may lack `nl2sql` NS until first apply; tenant_cd registry currently empty for this client.
