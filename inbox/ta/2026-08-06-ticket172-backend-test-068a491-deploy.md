---
id: inbox-ta-2026-08-06-ticket172-backend-test-068a491-deploy
agent: ta
ticket_id: 172
updated: 2026-08-06
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/37
  - https://github.com/yoosungung/nl2sql/actions/runs/31062265256
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# #172 test deploy backend test-068a491 (PR #37)

- merge_sha `068a491eee8e3f5fdba504f023cfcedd394b5e7e` · GHCR `nl2sql-backend:test-068a491` via publish run 31062265256 (`build-backend-image` success).
- `kubectl set image` + annotate `nl2sql.io/merge-sha` → Ready 1/1; `/api/health`+`/api/ready` 200; mcp `/ready` 200.
- MDL PVC kept: HEAD `5fe07689…` · 34 `*.model.json` (no reseed).
- tenant_cd registry `tenants=[]` → test overlay + publish-releases (not workflow_dispatch CD).
- Hand off: status QA · smoke expect sql|error+done → agent-ex 135; aa delta on PR #37.
