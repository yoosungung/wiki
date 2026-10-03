---
id: inbox-pm-admin-page-scroll
agent: pm
ticket_id: c2d5f98c-a83e-4414-8016-879951b398bc
updated: 2026-10-03
status: inbox
sources:
  - ticket:c2d5f98c-a83e-4414-8016-879951b398bc
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
  - ticket:900893c0-b570-496c-859a-ce201e3b57bc
  - https://stackoverflow.com/questions/30918777/overflow-auto-in-nested-flexboxes
---

# Factory SPA: `.main` overflow hidden clips pages without `.page-scroll`

- `.main { overflow: hidden; min-height: 0 }` + flex column means content not wrapped in `.page-scroll` (flex 1, overflow-y auto) is clipped — no body scroll.
- `/admin` put the users table inside `.page-header` (flex-shrink 0) so the list cannot scroll.
- Same clip class as Your work / Projects: keep chrome + page-header fixed, move the table into `.page-scroll`. Nested flex: min-height 0 on the scroll child.
- Do not set `.main` overflow visible (breaks board layout).
