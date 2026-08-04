---
id: inbox-ta-ticket60-deploying-test-ghcr-blocker
agent: ta
ticket_id: 60
updated: 2026-08-04
status: inbox
sources:
  - ticket:60
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - https://github.com/yoosungung/sw-factory/pull/2
---

# #60 Deploying Test blocked: GHCR push for cursor-agent-runner

- `tenant-cd-registry.json` tenants=[] → no workflow_dispatch CD; factory path is image rebuild per SETUP §4.
- Live `/opt/leantime-mcp` lacks `get_status_labels(project_id)`; main@a078367 (merge bc431747+) has the fix baked via Dockerfile `COPY leantime-mcp`.
- Pod has no docker; Jobs create=no. GHCR probe with Pod `GH_TOKEN` and Secret `ghcr-pull` → 401/403 (no packages write / invalid token).
- Need Eric: refresh GHCR push creds (or run `docker buildx … --push` from SETUP), then TA STS rollout + MCP/Kanban verify.
