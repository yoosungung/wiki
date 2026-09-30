---
id: inbox-sw-factory-timeline-status-dates
agent: sw-factory
ticket_id: ab2df6e6-584f-4d84-84f9-b54758117d46
updated: 2026-09-30
status: inbox
sources:
  - ticket:ab2df6e6-584f-4d84-84f9-b54758117d46
  - ARCHITECTURE.md
---

# Factory Timeline dates from status, not only manual range

- `GET …/timeline` still requires stored `date_from`/`date_to`. Empty fields are filled on create/PATCH (UTC `YYYY-MM-DD`).
- SPA Create used to send `date_from`/`date_to: null`; create treats null/empty as omitted so the form does not block auto-fill.
- Custom ranges on PATCH/create strings are kept. First `done` only replaces `date_to` when it still equals `created_at`'s date (auto open bar).
- Existing rows: migration `0007_timeline_status_dates` (activity history, else created_at / done updated_at / today).
