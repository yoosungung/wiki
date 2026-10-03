---
id: inbox-sw-factory-ticket-views-newest-first
agent: sw-factory
ticket_id: 84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
updated: 2026-10-03
status: inbox
sources:
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
---

# Factory ticket/project lists newest-first

- `GET /api/projects/:id/tickets` default is `created_at DESC, id DESC`; cursor uses the same direction (not ASC then FE reverse).
- Kanban columns display `sort_order DESC` so create-append (`MAX+1`) lands at the top; drag-saved sort_order is still the order key.
- Timeline **rows** are `date_from DESC`; gantt axis stays past→future LTR.
- `/projects` already used `created_at DESC`; tie-break is `id DESC`. Header stays put; `.page-scroll` owns overflow.
