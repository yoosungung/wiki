---
id: inbox-ta-nl2sql-551-prod-na-package-axis
agent: ta
ticket_id: 551
updated: 2026-08-12
status: inbox
sources:
  - ticket:551
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - https://github.com/yoosungung/nl2sql/blob/main/deploy/SETUP.md
---

# nl2sql #551 Deploying Prod = package axis N/A

- Ticket delivers Kaniko **test tip** path (`test-<sha>`), not a `vX.Y.Z` package cut.
- SETUP + wiki: Prod = `build-ghcr-images` + `publish-releases` package publish; **not** shared-cluster apply.
- AC3 / SETUP: `publish-releases tag=test-*` forbidden — do not use tip tag as prod package.
- Registry `tenant_cd.workflow=deploy.yml` is stale (file absent); tip CD is Kaniko/overlay.
- Feature Done evidence: test_* + qa: + aa: + `prod_* = N/A (package out of scope)` + tip re-smoke still green.
