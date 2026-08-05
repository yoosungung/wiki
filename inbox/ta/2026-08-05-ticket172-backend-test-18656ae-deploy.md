---
id: inbox-ta-2026-08-05-ticket172-backend-test-18656ae-deploy
agent: ta
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/35
  - https://github.com/yoosungung/nl2sql/actions/runs/30992730759
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# #172 test deploy backend test-18656ae (PR #35)

- merge_sha `18656aed…` · GHCR `nl2sql-backend:test-18656ae` via publish run 30992730759 (`build-backend-image` success).
- Rollout OK · Ready 1/1 · smoke Service `/api/health`+`/api/ready` → HTTP 200.
- tenant_cd registry empty; test-overlay + publish path (not workflow_dispatch CD).
- Live now has mcp lock fix + prior payload trim (PR #34 content on main).
