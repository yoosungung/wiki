---
id: inbox-ta-2026-08-10-ticket415-test-9ac4c82-deploy
agent: ta
ticket_id: 415
updated: 2026-08-10
status: inbox
sources:
  - ticket:415
  - https://github.com/yoosungung/nl2sql/pull/46
  - https://github.com/yoosungung/nl2sql/actions/runs/31353011752
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# nl2sql #415 Deploying Test: test-9ac4c82

- Registry `tenant_cd.workflow=deploy.yml` still missing on `yoosungung/nl2sql` → Test-Overlay path: `publish-releases` `tag=test-9ac4c82` + `kubectl set image` backend-only.
- `merge_sha` `9ac4c82` is ancestor of build `headSha` `bede626` (main ahead +3 incl. #391/#47).
- Live: `ghcr.io/yoosungung/nl2sql-backend:test-9ac4c82` · `/api/health`+`/api/ready` 200.
- Workflow overall `cancelled` after `build-backend-image` success (mcp not required for backend chat delta).
