---
id: inbox-ta-2026-08-10-ticket415-prod-9ac4c82-deploy
agent: ta
ticket_id: 415
updated: 2026-08-10
status: inbox
sources:
  - ticket:415
  - https://github.com/yoosungung/nl2sql/pull/46
  - https://github.com/yoosungung/nl2sql/actions/runs/31353387765
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# nl2sql #415 Deploying Prod: prod-9ac4c82

- Gates: `qa: e2e pass` (#1365) + `aa: security pass` (#1361) + prior test_* (#1360).
- Registry `deploy.yml` missing → `publish-releases` `tag=prod-9ac4c82` + `kubectl set image` backend-only (mcp cancelled after backend image success).
- Live: `ghcr.io/yoosungung/nl2sql-backend:prod-9ac4c82` · `/api/health`+`/api/ready` 200.
- Build head `bede626` includes merge_sha `9ac4c82` (ancestor).
