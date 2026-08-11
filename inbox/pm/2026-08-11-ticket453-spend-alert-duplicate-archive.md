---
id: inbox-pm-ticket453-spend-alert-duplicate-archive
agent: pm
ticket_id: 453
updated: 2026-08-11
status: inbox
sources:
  - ticket:453
  - ticket:310
  - ticket:447
  - https://github.com/yoosungung/sw-factory/pull/6
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
tags: ["spend-alert", "duplicate", "Archived"]
---

# Spend-alert #453 Archived (duplicate of #310)

- Eric @pm on #453: raise `SPEND_TOKENS_PER_CLIENT` 20M→100M (same decision as #310 #1641).
- Canonical work is on #310: PR #6 merged (`bdf4294…`); live CronJob still `20000000` awaiting TA apply.
- #453 snapshot (24h 197567025 vs old 100M threshold) is a cron sibling — Archived with pointer to #310 (same as #447).
- Do not self-Done spend-alerts; Archive only after human decision + canonical pointer.
