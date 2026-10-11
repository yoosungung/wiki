---
id: inbox-pm-crewrp-ios-due-closeout
agent: pm
ticket_id: b1478604-0dee-45ad-9400-824cac20e95f
updated: 2026-10-11
status: inbox
sources:
  - ticket:b1478604-0dee-45ad-9400-824cac20e95f
  - https://github.com/yoosungung/CrewRP/pull/7
  - https://github.com/yoosungung/CrewRP/commit/d2b5fb6e31b13ea0a4f1f71b6dc5029571607c9f
---

# CrewRP iOS due edit closeout

- Intent pass on PR#7 defensive silent-no-op fix; residual device AC confirmed by eric (other main changes).
- Main path that covers UX: `d2b5fb6` DatePicker DueOnField + `ensureDueDateField` on update when `projectMeta` loaded.
- Closed PR#7 without merge (stale vs title/body/assignee `updateTask`); edge `projectMeta == nil` silent return may still exist on main — not reopened while AC met.
