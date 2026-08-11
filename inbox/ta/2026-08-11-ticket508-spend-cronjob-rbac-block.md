---
id: inbox-ta-ticket508-spend-cronjob-rbac-block
agent: ta
ticket_id: 508
updated: 2026-08-11
status: inbox
sources:
  - ticket:508
  - wiki/Engineering/AI-Native-Engineering/Spend-Alert-Human-Approval-Triage.md
  - https://github.com/yoosungung/sw-factory (deploy/k8s/base/agent-rbac.yaml)
tags: ["spend-alert", "SPEND_TOKENS_PER_CLIENT", "RBAC", "cronjobs"]
---

# #508: TA cannot patch cursorbridge-spend-alert CronJob

- Live CronJob still `SPEND_TOKENS_PER_CLIENT=20000000`; git/base already `100000000` (e63fd4c / cronjob-spend-alert.yaml).
- SA `system:serviceaccount:sw-factory:cursor-agent-ta` has batch cronjobs/jobs **get/list/watch only** (`cursor-agent-ta-operator` ClusterRole). Patch attempt → Forbidden.
- Deployments mutate OK; CronJob apply is platform/Eric lane unless RBAC is expanded.
- Closeout of #480/#310 already Done when TA ran; remaining AC is live env=100M.
- Eric one-liner after approve: `kubectl -n sw-factory patch cronjob cursorbridge-spend-alert --type=json -p='[{"op":"replace","path":"/spec/jobTemplate/spec/template/spec/containers/0/env/0/value","value":"100000000"}]'` then verify jsonpath env.
