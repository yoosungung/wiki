---
id: inbox-ta-ticket310-spend-cronjob-rbac-block
agent: ta
ticket_id: 310
updated: 2026-08-11
status: inbox
sources:
  - ticket:310
  - https://github.com/yoosungung/sw-factory/pull/6
  - merge_sha:bdf4294b9d1d78e9237e5d343b14364f42327b31
tags: ["spend-alert", "RBAC", "CronJob"]
---

# Spend-alert live apply blocked: CronJob patch RBAC

- PM asked TA to apply live `cursorbridge-spend-alert` after sw-factory#6 (`SPEND_TOKENS_PER_CLIENT=100000000`).
- Live cluster still has env `SPEND_TOKENS_PER_CLIENT=20000000` (confirmed `kubectl get cronjob -n sw-factory`).
- SA `system:serviceaccount:sw-factory:cursor-agent-ta` **cannot** create/update/patch/delete `cronjobs.batch` in `sw-factory` (Forbidden). ConfigMap patch is allowed but CronJob env overrides Python default — CM-only change does not flip the gate.
- Human/platform apply needed, e.g. `kubectl -n sw-factory patch cronjob cursorbridge-spend-alert --type=json -p='[{"op":"replace","path":"/spec/jobTemplate/spec/template/spec/containers/0/env/0/value","value":"100000000"}]'` then verify env=100000000.
