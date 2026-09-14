---
id: inbox-ta-nf-1986-tenant-cd-prod
agent: ta
ticket_id: 1986
updated: 2026-09-14
status: inbox
sources:
  - ticket:1986
  - https://github.com/yoosungung/nl2sql/pull/151
---

# nl2sql #1986 Deploying Prod (prod-sha promote)

- Shared-cluster NF promote uses GHCR `prod-<shortsha>` (same pattern as `prod-401b55b`), not semver `publish-releases` (no RELEASE bump for this NF).
- Kaniko Job `nl2sql-kaniko-backend-prod-50e2b81` → roll `nl2sql/nl2sql-backend` → smoke `/api/health`+`/api/ready` 200.
- mcp init binary pin left on published `v*`/`prod-*` release assets (do not retarget to tip/`test-*`).
