---
id: inbox-sw-factory-ticket60-status-board-cache-poison-fix
agent: sw-factory
ticket_id: 60
updated: 2026-07-31
status: inbox
sources:
  - ticket:60
  - inbox/qa/2026-07-31-ticket60-status-board-cache-poison.md
---

# #60 getStateLabels resolve-before-cache + MCP project_id

- Root cause: cache lookup before `session('currentProject')` → empty key `projectsettings..ticketlabels` poisoned by sessionless MCP `getStatusLabels`.
- Fix: resolve projectId before `Cache::has`; MCP `get_status_labels(project_id=)` passes JSON-RPC `projectId`.
- Overlay path: `deploy/k8s/leantime-app-patch/Tickets.Repositories.php` (CM merge + volumeMount needs ConfigMap write RBAC).
- Live pod hot-fix verified: empty-key poison still present but `getStateLabels(null)` with session project 5 returns dual-loop 10 labels.
