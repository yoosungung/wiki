---
id: inbox-ta-ticket453-spend-alert-apply-rbac-block
agent: ta
ticket_id: 453
updated: 2026-08-11
status: inbox
sources:
  - ticket:453
  - ticket:310
  - https://github.com/yoosungung/sw-factory/pull/6
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
tags: ["spend-alert", "SPEND_TOKENS_PER_CLIENT", "RBAC", "CronJob"]
---

# #453: live CronJob still 20M — TA cannot patch

- Eric decision (same as #310): `SPEND_TOKENS_PER_CLIENT` 20M → 100M. Git merged: PR #6 / `bdf4294`.
- Live `cursorbridge-spend-alert` env still `20000000` (read-only confirm).
- SA `cursor-agent-ta` Forbidden on `patch cronjobs` in `sw-factory` — needs human/platform apply.
- #453 is duplicate of Approval/#310 lane; do not Done until live env is 100M.
