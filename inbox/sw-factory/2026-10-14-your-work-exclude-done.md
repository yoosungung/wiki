---
id: inbox-sw-factory-your-work-exclude-done
agent: sw-factory
ticket_id: 9d528a70-fbd4-4e8e-a87b-6fa536e690f9
updated: 2026-10-14
status: inbox
sources:
  - ticket:9d528a70-fbd4-4e8e-a87b-6fa536e690f9
  - ARCHITECTURE.md
---

# Your work Assigned — exclude_done API

- `GET /api/projects/:id/tickets?exclude_done=true` drops all `project_statuses.category=done` (any age/key); takes precedence over soft-archive.
- Your work Assigned tab passes `assignee_id=me&exclude_done=true`; Created/Viewed/Directory/kanban unchanged.
- Prefer API exclude over FE filter so pagination is not filled by recent done.
