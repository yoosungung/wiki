---
id: inbox-sw-factory-timeline-list-timeline-4col
agent: sw-factory
ticket_id: 54683314-7fe6-4d5d-8a13-f19985b89505
updated: 2026-10-15
status: inbox
sources:
  - ticket:54683314-7fe6-4d5d-8a13-f19985b89505
  - https://github.com/yoosungung/sw-factory/pull/40
---

# Timeline list-row 4-column modifier

- Shared `.list-row` stays `160px 1fr 120px` (3-col) for clients/other lists.
- Timeline rows use `.list-row.list-timeline` → `auto minmax(0,10rem) minmax(0,1fr) auto` so title is the wide column and status stays on one line (>768px).
- Mobile `<768px`: `.list-row.list-timeline` stacks to `1fr` with base `.list-row`.
