---
id: inbox-candidate-ticket176-pass-ab-exit99-setsid
agent: candidate
ticket_id: 176
updated: 2026-08-05
status: inbox
sources:
  - ticket:176
  - leantime:project:7:candidate.win
---

# Pass AB exit_code=99 — setsid + bash invoke

- CronJob `kubectl exec` → launcher; skill scripts seed as mode **0644**. Bare `exec "$WORKER"` → Permission denied (126) → empty worker.log → monitor exit **99**.
- `nohup ... &` alone also dies when exec session ends; use **`setsid`** + **`exec bash "$@"`** and redirect to durable `worker.log`.
- PVC hotfix on candidate pod is live; ConfigMap `persona-candidate` patch is **Forbidden** for pod SA — platform must re-seed from agents.yaml or admin patch, else next seed overwrites.
- Regression: `candydate-cron/scripts/test_pass_ab_launcher_detach.sh`.
