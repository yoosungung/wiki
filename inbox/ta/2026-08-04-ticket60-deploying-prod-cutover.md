---
id: inbox-ta-ticket60-deploying-prod-cutover
agent: ta
ticket_id: 60
updated: 2026-08-04
status: inbox
sources:
  - ticket:60
  - wiki/Engineering/AI-Native-Engineering/Sessionless-MCP-Status-Label-Cache-Poison.md
  - wiki/Engineering/Infrastructure-and-DevOps/Helm-App-Patch-ConfigMap-Persistence.md
  - https://github.com/yoosungung/sw-factory/pull/2
---

# #60 Deploying Prod cutover — overlay + dual-loop

- Factory cluster is prod for this ticket (`tenant_cd` N/A; registry tenants=[]).
- CM `leantime-app-patch` has 12 keys incl. `Tickets.Repositories.php`; Deploy volumeMount → `/…/Tickets/Repositories/Tickets.php` (subPath). Live pod grep: resolve-before-cache (`session('currentProject')` before `Cache::has`).
- Agent STS digest `sha256:84c40f78…063f6`; image source has `get_status_labels(project_id?)`.
- After sessionless poison×5 (seed-6), JSON-RPC `getStatusLabels(projectId=5)`×8 → dual-loop 10 labels STABLE (ids include 10/11/12/13).
- Residual: live `/opt/leantime-venv/bin/leantime-mcp` fails import (`McpError` vs `MCPError`); agents use JSON-RPC Bearer. Non-blocking for Kanban AC.
