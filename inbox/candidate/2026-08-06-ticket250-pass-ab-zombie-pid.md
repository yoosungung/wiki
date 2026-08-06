---
id: inbox-candidate-2026-08-06-ticket250-pass-ab-zombie-pid
agent: candidate
ticket_id: 250
updated: 2026-08-06
status: inbox
sources:
  - ticket:250
  - ticket:238
  - ticket:176
  - wiki/Engineering/Infrastructure-and-DevOps/PVC-Nonexec-Script-Setsid-Bash.md
---

# Pass AB exit 99 — zombie PID + cron SSoT

- `kill -0` is true for `/proc` `State=Z`; monitor/launcher must use zombie-safe `is_pid_running` or status stays `running` after successful Pass A+B.
- ConfigMap reseed can restore bare `nohup`/`exec "$@"` over PVC `setsid+bash` hotfix → empty worker.log → monitor exit 99 (see PVC-Nonexec-Script-Setsid-Bash).
- Durable fix: repo `agent/cron/` SSoT; skill path = thin `exec` shim to repo; worker EXIT-trap completion writer.
