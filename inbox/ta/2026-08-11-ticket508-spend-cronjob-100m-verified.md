---
id: inbox-ta-ticket508-spend-cronjob-100m-verified
agent: ta
ticket_id: 508
updated: 2026-08-11
status: inbox
sources:
  - ticket:508
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
---

# #508 live SPEND_TOKENS_PER_CLIENT=100M verified

- Live CronJob `sw-factory/cursorbridge-spend-alert` env `SPEND_TOKENS_PER_CLIENT=100000000` (matches repo `e63fd4c`).
- Expected alert threshold: 5×100M=500M.
- TA SA still cannot `patch`/`update` cronjobs (`kubectl auth can-i` = no); apply was done outside TA RBAC (likely Eric).
- Stale Approval spend tickets #480/#310 already Done — no closeout write needed.
