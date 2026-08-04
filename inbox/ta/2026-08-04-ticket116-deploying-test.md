---
id: inbox-ta-ticket116-deploying-test
agent: ta
ticket_id: 116
updated: 2026-08-04
status: inbox
sources:
  - ticket:116
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - https://github.com/yoosungung/nl2sql/pull/26
---

# #116 Deploying Test — overlay path (registry empty)

- `tenant-cd-registry.json` tenants=[] → no workflow_dispatch; nl2sql test = `deploy/k8s/overlays/test/apply.sh`.
- merge_sha `5e9ffd5` is load harness only (in-process ASGI); cluster images remain `nl2sql-backend:v0.1.1`.
- Preserve existing `MCP_SHARED_TOKEN` when re-applying; Service smoke uses ports 8080/8800 (not 80).
- Auth: `POST /api/chat` without identity → 401; health/ready → 200.
