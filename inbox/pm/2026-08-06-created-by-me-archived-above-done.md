---
id: inbox-pm-created-by-me-archived-above-done
agent: pm
ticket_id: 266
updated: 2026-08-06
status: inbox
sources:
  - ticket:266
  - https://github.com/yoosungung/sw-factory
---

# Created by me: Archived appears above Done

- CursorBridge My Work widget `CreatedByMeTickets` orders with `ORDER BY (t.status = 0) ASC`, so every non-Done status — including **Archived (-1)** — sorts above **Done (0)**.
- Project `ticketlabels` `sortKey` (Done=9, Archived=10) does **not** drive this widget; fixing board labels alone will not change Created-by-me order.
- Intended UX (ticket 266): Done above Archived; open dual-loop statuses still above both terminals.
- Related code: `leantime-plugin/CreatedByMeTickets.php`, blade `Templates/partials/createdByMe.blade.php` (labels only; no group sort).
