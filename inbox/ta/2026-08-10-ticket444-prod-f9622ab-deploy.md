---
id: inbox-ta-2026-08-10-ticket444-prod-f9622ab-deploy
agent: ta
ticket_id: 444
updated: 2026-08-10
status: inbox
sources:
  - ticket:444
  - https://github.com/yoosungung/nl2sql/pull/51
  - https://github.com/yoosungung/nl2sql/actions/runs/31358929831
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# nl2sql #444 Deploying Prod: prod-f9622ab

- Gates: QA Outcome PASS (#1487) + aa: security pass (#1483) + prior test_* (#1481/#1482).
- Registry `deploy.yml` missing → `publish-releases` `tag=prod-f9622ab` + `kubectl set image` backend-only (mcp cancelled after backend image success).
- Live: `ghcr.io/yoosungung/nl2sql-backend:prod-f9622ab` · `/api/health`+`/api/ready` 200 (pod + Service FQDN).
- Live ANALYST_TOOLS includes `get_column_values` + `describe_columns` (import verify).
