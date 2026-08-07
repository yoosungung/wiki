---
id: inbox-ta-persona-candidate-thin-shim-seed
agent: ta
ticket_id: 308
updated: 2026-08-07
status: inbox
sources:
  - ticket:308
  - wiki/Engineering/Infrastructure-and-DevOps/PVC-Nonexec-Script-Setsid-Bash.md
  - https://github.com/yoosungung/sw-factory/pull/5
---

# persona-candidate candydate-cron seed → thin shims

- Live hotfix on PVC was already thin shim (`install_skill_shims.sh`); ConfigMap `persona-candidate` still had stale full copies (`nohup`, multi-KB) — next seed-persona overwrite would restore exit 99.
- TA patched CM keys for launcher/monitor/worker/pass_d/paths/leantime_cron_report(+test detach) to `exec bash|python3 …/agent/cron/…` (~130B).
- Tracked guard: sw-factory PR #5 (`test_candydate_cron_persona_shims.py` + SETUP.md). Local gitignored `deploy/personas/candidate/` on render host must be regenerated with `install_skill_shims.sh` before next `render-agents` apply, or CM regresses.
