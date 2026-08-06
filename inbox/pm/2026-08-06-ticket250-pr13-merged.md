---
id: inbox-pm-2026-08-06-ticket250-pr13-merged
agent: pm
ticket_id: 250
updated: 2026-08-06
status: inbox
sources:
  - ticket:250
  - https://github.com/berryking404/candidate.win/pull/13
  - wiki/Engineering/Infrastructure-and-DevOps/PVC-Nonexec-Script-Setsid-Bash.md
---

# #250 PR#13 merged — Pass AB cron SSoT

- Merged `fix(250): Pass AB cron SSoT + zombie-safe PID` → merge_sha `3c39509b1024be344c35e9fe6049e1d3eaa1f963`.
- Root cause: ConfigMap reseed can wipe PVC setsid+bash; `kill -0` true on State=Z → false exit 99.
- Fix in repo `agent/cron/`; CronJob still calls skill-path scripts — those must remain thin `exec` shims to repo (reseed overwrite → Eric Approval).
- tenant_cd N/A (cron ops).
