---
id: inbox-pm-2026-08-06-spend-alert-triage
agent: pm
ticket_id: 212
updated: 2026-08-06
status: inbox
sources:
  - ticket:212
  - ticket:208
  - ticket:207
  - ticket:184
  - ticket:169
  - ticket:165
  - ticket:164
  - ticket:111
---

# Spend alert triage (CURSOR_API_KEY)

- Cron creates New `[Spend alert]` tickets (tags `cron,spend-alert,factory`) when 24h CURSOR_API_KEY usage exceeds threshold; assignee may be an unknown editorId (e.g. 13).
- PM catch-up action: pick latest open alert as canonical → `Waiting for Approval` + assignee Eric + `@eric` ask (ack vs raise threshold vs cut agent load). List older New siblings as duplicates; do not Done without Eric decision.
- Cost/budget judgment is human-only (not agent Blocked loops).
