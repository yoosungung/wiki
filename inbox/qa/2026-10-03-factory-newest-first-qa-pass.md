---
id: inbox-qa-factory-newest-first-qa-pass
agent: qa
ticket_id: 84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
updated: 2026-10-03
status: inbox
sources:
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
  - https://factory.askwho.net/api/health
---

# factory.askwho.net newest-first QA

- Live `GET /api/projects` is `created_at DESC` (UniTutorAI → CrewRP → sw-factory).
- Live `GET /api/projects/:id/tickets` is `created_at DESC`; kanban columns `sort_order DESC`; timeline rows `date_from DESC`.
- Prod `/projects`: `main.main` overflow hidden, `.page-scroll` overflow-y auto, header stays above the scrolling grid.
- Local Playwright `e2e/projects-newest.spec.ts` + `e2e/fe3-fe5.spec.ts` green (header pin + newest List/Board + Your work `.page-scroll`).
