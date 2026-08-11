---
id: inbox-ta-ticket508-spend-cronjob-applied
agent: ta
ticket_id: 508
updated: 2026-08-11
status: inbox
sources:
  - ticket:508
  - ticket:480
  - ticket:310
  - inbox/ta/2026-08-11-ticket508-spend-cronjob-rbac-block.md
  - https://github.com/yoosungung/sw-factory/commit/e63fd4c8f6bccf5ac5954a53b1ef18ac6209216a
tags: ["spend-alert", "SPEND_TOKENS_PER_CLIENT", "CronJob"]
---

# #508: live SPEND_TOKENS_PER_CLIENT=100M verified

- Eric applied cluster CronJob; TA re-verified `kubectl -n sw-factory get cronjob cursorbridge-spend-alert` → `SPEND_TOKENS_PER_CLIENT=100000000`.
- Git already at 100M since `e63fd4c` (`deploy/k8s/base/cronjob-spend-alert.yaml` + overlay `patch-spend.yaml`). No further repo change needed.
- TA still cannot patch CronJobs (`can-i patch/update cronjobs` = no); apply remains Eric/platform lane.
- #480 / #310 already Done; closeout comments left noting 500M threshold.
- Effective alert threshold: 5 clients × 100M = 500M.
