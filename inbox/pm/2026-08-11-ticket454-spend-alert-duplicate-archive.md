---
id: inbox-pm-ticket454-spend-alert-duplicate-archive
agent: pm
ticket_id: 454
updated: 2026-08-11
status: inbox
sources:
  - ticket:454
  - ticket:310
  - ticket:447
  - ticket:453
  - https://github.com/yoosungung/sw-factory/pull/6
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
  - https://cursor.com/changelog/05-04-26
tags: ["spend-alert", "duplicate", "Archived"]
---

# Spend-alert #454 Archived (duplicate of #310)

- TA @pm FYI: Done regression refused; status stays Archived(-1) as cron sibling of canonical #310.
- Facts: 24h `218148350` vs old threshold `100000000` (5×20M). Human decision already on #310: `SPEND_TOKENS_PER_CLIENT` 20M→100M; PR #6 `bdf4294…` merged.
- Live CronJob apply remains on #310 only — no reopen/git-ship on #454. Soft-limit pattern (Cursor May 2026) supports raise-threshold over hard-stop.
