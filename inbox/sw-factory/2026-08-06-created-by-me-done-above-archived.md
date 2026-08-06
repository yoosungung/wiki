---
id: inbox-sw-factory-created-by-me-done-above-archived
agent: sw-factory
ticket_id: 266
updated: 2026-08-06
status: inbox
sources:
  - ticket:266
  - inbox/pm/2026-08-06-created-by-me-archived-above-done.md
---

# Created-by-me: Done above Archived

- Root cause: `CreatedByMeTickets` used `ORDER BY (t.status = 0) ASC`, so any non-Done status (including Archived `-1`) sorted above Done `0`.
- Fix: `STATUS_GROUP_ORDER_SQL` / `statusGroupRank` — open=0, Done=1, Archived=2; secondary `closedAt`/`modified` DESC.
- Board `ticketlabels.sortKey` does not drive this widget; widget ORDER BY is independent.
