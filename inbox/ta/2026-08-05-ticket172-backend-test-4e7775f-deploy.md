---
id: inbox-ta-2026-08-05-ticket172-backend-test-4e7775f-deploy
agent: ta
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/36
  - https://github.com/yoosungung/nl2sql/actions/runs/30994168080
---

# #172 test deploy backend test-4e7775f (PR #36)

- merge_sha `4e7775fc…` · GHCR `nl2sql-backend:test-4e7775f` via publish run 30994168080 (`build-backend-image` success).
- Rollout OK · Ready 1/1 · smoke `/api/health`+`/api/ready` → HTTP 200.
- MDL PVC seed (0 models / pass_rate>0) deferred — hang-fix image first.
