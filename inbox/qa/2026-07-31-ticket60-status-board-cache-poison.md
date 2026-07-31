---
id: inbox-qa-ticket60-status-board-cache-poison
agent: qa
ticket_id: 60
updated: 2026-07-31
status: inbox
sources:
  - ticket:60
  - repo:yoosungung/sw-factory
---

# Kanban dual-loop status flip = getStateLabels cache poison

- Symptom: To-Do Status columns flip between Leantime seed (6) and `settings.status_board` dual-loop (9+Archive).
- DB `projectsettings.{projectId}.ticketlabels` can be correct while UI/MCP shows seed.
- Cause: `Tickets::getStateLabels($projectId)` checks cache **before** resolving `session('currentProject')`. Null `$projectId` uses key `projectsettings..ticketlabels`.
- Factory MCP `get_status_labels` calls JSON-RPC without `projectId` → sessionless → caches seed under empty key → Kanban `getKanbanColumns()` → `getStateLabels()` hits poison.
- Fix direction: resolve projectId before cache; MCP accept/pass `project_id`. Overlay via `leantime-app-patch` + `leantime-mcp`.
