---
id: inbox-pm-ticket453-spend-alert-duplicate-archive
agent: pm
ticket_id: 453
updated: 2026-08-11
status: inbox
sources:
  - ticket:453
  - ticket:310
  - https://github.com/yoosungung/sw-factory/pull/6
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
tags: ["spend-alert", "duplicate", "Archived"]
---

# Spend-alert #453 Archived (duplicate of #310)

- Eric @pm on #453: `SPEND_TOKENS_PER_CLIENT` 20M→100M (same decision as #310).
- Code already on main via PR #6 (`merge_sha` bdf4294…); manifests/default = 100M.
- Live CronJob `cursorbridge-spend-alert` still `SPEND_TOKENS_PER_CLIENT=20000000` — apply remains on canonical #310 (@ta).
- #453 archived as duplicate sibling after human decision recorded.
