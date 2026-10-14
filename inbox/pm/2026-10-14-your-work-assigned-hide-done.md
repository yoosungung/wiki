---
id: inbox-pm-your-work-assigned-hide-done
agent: pm
ticket_id: 9d528a70-fbd4-4e8e-a87b-6fa536e690f9
updated: 2026-10-14
status: inbox
sources:
  - ticket:9d528a70-fbd4-4e8e-a87b-6fa536e690f9
  - frontend/ia/pages.md
---

# Your work Assigned to me — hide category=done

- Your work Assigned to me currently only soft-excludes archived Done (≥7d via `include_archived` / `archivedDoneFilter`); recent done still appear.
- Product ask: hide all `project_statuses.category=done` from Assigned to me (not Created/Viewed/kanban).
- Prefer list API exclude for pagination; FE-only filter is fallback with empty-page risk.
