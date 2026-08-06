---
id: inbox-pm-2026-08-06-ticket238-pass-ab-cron-triage
agent: pm
ticket_id: 238
updated: 2026-08-06
status: inbox
sources:
  - ticket:238
  - ticket:176
---

# Pass AB daily cron exit 99 triage (#238)

- Same signature as #176: async fail, `exit_code=99`, process gone before completion status, missing `/tmp/com.candydate.agent.log`.
- PM unassigned triage: assignee=candidate, status=In Progress; investigate launcher/log path vs yesterday setsid+OPENAI fix regression.
- Do not re-open #176; keep evidence on #238.
