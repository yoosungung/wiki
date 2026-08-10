---
id: inbox-ta-2026-08-10-ticket444-test-f9622ab-deploy
agent: ta
ticket_id: 444
updated: 2026-08-10
status: inbox
sources:
  - ticket:444
  - https://github.com/yoosungung/nl2sql/pull/51
  - https://github.com/yoosungung/nl2sql/actions/runs/31358390286
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# #444 Deploying Test: test-f9622ab

- PR #51 MERGED · merge_sha `f9622abdac97569cc5121793e4d8cfda49c1d366`.
- Registry `deploy.yml` missing → Test-Overlay: `publish-releases` `tag=test-f9622ab` (run 31358390286; `build-backend-image` success; mcp cancelled after).
- `kubectl set image` `nl2sql-backend` → `ghcr.io/yoosungung/nl2sql-backend:test-f9622ab` · rollout OK.
- Smoke: `/api/health`+`/api/ready` HTTP 200 (Service FQDN).
- Live ANALYST_TOOLS includes `get_column_values` + `describe_columns` (pod exec).
- Board: status QA · assignee qa — next live Trace re-QA + AA security.
