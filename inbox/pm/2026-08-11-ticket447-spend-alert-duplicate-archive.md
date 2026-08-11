---
id: inbox-pm-ticket447-spend-alert-duplicate-archive
agent: pm
ticket_id: 447
updated: 2026-08-11
status: inbox
sources:
  - ticket:447
  - ticket:310
  - https://github.com/yoosungung/sw-factory/pull/6
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
tags: ["spend-alert", "duplicate", "Archived"]
---

# Spend-alert #447 Archived (duplicate of #310)

- TA @pm FYI: premature Done reopen was correct (human-only spend-alert).
- Canonical decision is on #310: Eric chose raise `SPEND_TOKENS_PER_CLIENT` 20M→100M; PR #6 merged.
- #447 snapshot (24h 170147476 vs old threshold 100000000) is a duplicate sibling — Archived with pointer to #310.
- Live CronJob still showed `SPEND_TOKENS_PER_CLIENT=20000000` at triage time; cluster apply remains on #310 lane (not this ticket).
