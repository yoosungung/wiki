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

# nl2sql #444 Deploying Test: test-f9622ab

- Registry `tenant_cd.workflow=deploy.yml` still missing on `yoosungung/nl2sql` → Test-Overlay: `publish-releases` `tag=test-f9622ab` + `kubectl set image` backend-only.
- `merge_sha` `f9622abdac97569cc5121793e4d8cfda49c1d366` (PR #51 squash/merge — on-demand describe tools + AA F2 cap=8).
- Live: `ghcr.io/yoosungung/nl2sql-backend:test-f9622ab` · `/api/health`+`/api/ready` 200.
- Pod verify: `ANALYST_TOOLS` includes `get_column_values` + `describe_columns`.
- Handed to QA (12)/qa + @aa for live Trace / security re-gate.
