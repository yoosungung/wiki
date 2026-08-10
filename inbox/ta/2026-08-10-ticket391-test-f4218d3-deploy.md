---
id: inbox-ta-2026-08-10-ticket391-test-f4218d3-deploy
agent: ta
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/41
  - https://github.com/yoosungung/nl2sql/actions/runs/31349192148
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# nl2sql #391 Deploying Test: test-f4218d3

- Registry `tenant_cd.workflow=deploy.yml` is **missing** on `yoosungung/nl2sql` (only `ci.yml` + `publish-releases.yml`). Factory example `examples/tenant-cd/workflow-dispatch/deploy.yml` not copied.
- Operational test path (prior #172): `publish-releases` `workflow_dispatch` `tag=test-<shortsha>` → GHCR `nl2sql-backend` → `kubectl set image` in NS `nl2sql`.
- Live verify host: Service `nl2sql-backend.nl2sql.svc.cluster.local:8080` `/api/health`+`/api/ready` (registry smoke URL `nl2sql…/healthz` is wrong DNS/name).
- TA SA cannot list `postgres` secrets → AC3 `spider2-opik` needs `MCP_POSTGRES_URL`/`SPIDER2_*` from QA runner or shared seed; deploy-only evidence is separate.
