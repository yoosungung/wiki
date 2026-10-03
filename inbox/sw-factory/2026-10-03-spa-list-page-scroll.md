---
id: inbox-sw-factory-spa-list-page-scroll
agent: sw-factory
ticket_id: 900893c0-b570-496c-859a-ce201e3b57bc
updated: 2026-10-03
status: inbox
sources:
  - ticket:900893c0-b570-496c-859a-ce201e3b57bc
---

# SPA list pages need a page scrollport under `.main overflow: hidden`

- `.main { overflow: hidden }` is for board column layout. Do not set it to visible.
- `.content-panel.tableish { overflow: visible }` plus hidden `.main` clips long grids (Your work).
- Pattern: keep header/tabs outside, wrap the list in `.page-scroll` (`flex: 1; min-height: 0; overflow-y: auto`), same idea as Issue `.drawer-body`.
