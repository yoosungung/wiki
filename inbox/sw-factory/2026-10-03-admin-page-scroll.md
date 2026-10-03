---
id: inbox-sw-factory-admin-page-scroll
agent: sw-factory
ticket_id: c2d5f98c-a83e-4414-8016-879951b398bc
updated: 2026-10-03
status: inbox
sources:
  - ticket:c2d5f98c-a83e-4414-8016-879951b398bc
  - inbox/pm/2026-10-03-admin-page-scroll.md
---

# Factory SPA: remaining list pages use header + `.page-scroll`

- `/admin` users table must sit in `.page-scroll`, not inside `.page-header` (Create space stays in the header).
- Same clip: `/account`, `/teams`, `/filters`, Space/Project settings People (`settings-main.page-scroll`; `.main > .settings-layout` fills height). Search already had `.page-scroll`.
- Do not set `.main { overflow: visible }` — board layout depends on hidden.
