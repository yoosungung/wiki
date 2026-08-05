---
id: inbox-ta-2026-08-05-ticket172-backend-image-crash
agent: ta
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/34
  - https://github.com/yoosungung/nl2sql/actions/runs/30991883013
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# #172 test backend image CrashLoop — mcp ImportError

- merge_sha `06c065ac…` (PR #34) published as GHCR tag `test-06c065a` via publish-releases run 30991883013 (`build-backend-image` success).
- `kubectl set image` → new pod CrashLoopBackOff: `ImportError: cannot import name 'streamablehttp_client' from 'mcp.client.streamable_http'`.
- Live restored to `ghcr.io/yoosungung/nl2sql-backend:v0.1.1` (health/ready 200). Payload trim not live.
- tenant_cd registry empty; used test-overlay + publish path (not workflow_dispatch CD).
- Need nl2sql Dockerfile/lock pin for `mcp` SDK so image imports match `mcp_client.py`.
