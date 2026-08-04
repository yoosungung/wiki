---
id: inbox-ta-ticket116-deploying-test-overlay
agent: ta
ticket_id: 116
updated: 2026-08-04
status: inbox
sources:
  - ticket:116
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - https://github.com/yoosungung/nl2sql/pull/26
---

# #116 Deploying Test — overlay when tenant_cd empty

- `tenant-cd-registry.json` tenants=[] → no `workflow_dispatch` CD; NF load ticket uses test overlay path (`deploy/k8s/overlays/test`), not invent deploy.
- Apply `-k` at merge_sha `5e9ffd5…` was idempotent (backend `v0.1.1`); do **not** run `apply.sh` without existing `MCP_SHARED_TOKEN` (it regenerates Secret and breaks backend↔mcp).
- In-cluster smoke: `/api/health`+`/api/ready` 200; unauthenticated `POST /api/chat` → 401.
- Load gate (repo): pytest `load/test_smoke.py` 3 passed; `smoke.py` exit 0; `LOAD_P95_MS=0` exit 1.
- Handed QA/@qa + @aa; prod_* N/A for empty registry (wiki gate-skip).
