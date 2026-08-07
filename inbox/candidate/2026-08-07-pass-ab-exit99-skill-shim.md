---
id: inbox-candidate-pass-ab-exit99-skill-shim
agent: candidate
ticket_id: 308
updated: 2026-08-07
status: inbox
sources:
  - ticket:308
  - wiki/Engineering/Infrastructure-and-DevOps/PVC-Nonexec-Script-Setsid-Bash.md
  - wiki/Engineering/Infrastructure-and-DevOps/Cron-Monitor-Zombie-PID-Check.md
---

# Pass AB exit 99 — skill PVC stale full copy

- Symptom: monitor exit 99 + empty `worker.log` when skill-path launcher still has `nohup` + bare `exec "$@"` on 0644 worker (Permission denied before first log line).
- Durable fix: repo `agent/cron/` is SSoT (`setsid` + `exec bash`); skill scripts must be thin shims via `agent/cron/install_skill_shims.sh <skill-scripts-dir>`.
- ConfigMap/agents.yaml reseed that restores full stale copies will regress exit 99 — keep shims in seed.
