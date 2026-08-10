---
id: inbox-candidate-pass-ab-post-deploy-preflight
agent: candidate
ticket_id: 308
updated: 2026-08-10
status: inbox
sources:
  - ticket:308
  - wiki/Engineering/Infrastructure-and-DevOps/PVC-Nonexec-Script-Setsid-Bash.md
---

# Pass AB post-deploy preflight (Eric render-agents + STS restart)

- After 2026-08-10 Eric deploy reflection, `persona-candidate` CM candydate-cron scripts remain thin `exec bash|python3 …/agent/cron/…` shims (no `nohup` full copy).
- PVC `/cursor-home/.cursor/skills/candydate-cron/scripts/` matches CM thin shims (seed reflected).
- Last scheduled launch `candydate-pass-ab-launch-29770740` (2026-08-09T03:00Z): Complete; `worker.log` has start+finishing lines; `state.env` status=done exit_code=0 run_id=20260809T030001Z-54475.
- Next observation window: `candydate-pass-ab-launch` cron `0 12 * * *` → 2026-08-10T03:00:00Z; verify exit≠99 and non-empty worker start/finish.
