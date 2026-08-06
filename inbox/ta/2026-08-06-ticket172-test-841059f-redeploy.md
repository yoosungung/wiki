---
id: inbox-ta-2026-08-06-ticket172-test-841059f-redeploy
agent: ta
ticket_id: 172
updated: 2026-08-06
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/38
  - https://github.com/yoosungung/nl2sql/actions/runs/31064746117
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# nl2sql #172 test redeploy via publish-releases + set image

- tenant_cd registry lists `deploy.yml` but workflow is absent; test path = `Publish to nl2sql-releases` (`tag=test-<shortsha>`) then `kubectl set image` on `nl2sql/nl2sql-backend`.
- PR #38 merge_sha `841059f5178bce8f239d2a6de96423b0b371e98e` → GHCR `ghcr.io/yoosungung/nl2sql-backend:test-841059f` (run 31064746117 success).
- In-cluster smoke uses Service DNS `nl2sql-backend.nl2sql.svc.cluster.local:8080` (`/api/health`, `/api/ready`) — registry `nl2sql.nl2sql.svc.../healthz` does not resolve.
- mcp deploy left unchanged when backend-only product delta (search compact slim); MDL PVC keep/no reseed.
