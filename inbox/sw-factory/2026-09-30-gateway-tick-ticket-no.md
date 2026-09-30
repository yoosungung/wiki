---
id: inbox-sw-factory-gateway-tick-ticket-no
agent: sw-factory
ticket_id: ea2d1b81-5582-4a25-a7dc-e9b2fc22b3e1
updated: 2026-09-30
status: inbox
sources:
  - ticket:ea2d1b81-5582-4a25-a7dc-e9b2fc22b3e1
  - frontend/src/components/issue/IssuePanel.tsx issueKey
---

# Gateway tick `ticket_no` = UI issueKey

- Factory UI ticket display key: `issueKey(project.name, ticket.id)` → e.g. `sw-factory` + `ea2d1b81-…` = `SWF-EA2D` (not sequential, not raw UUID alone).
- Gateway `msg: tick` `dispatched[]` should include `ticket_no` (that format) plus `ticket_id` UUID and `agent_id` session for operator correlation.
- Prefix needs project name: gateway caches `GET /api/projects/:id` (no Worker schema change).
