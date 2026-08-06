---
id: inbox-pm-2026-08-06-ticket250-pass-ab-cron-triage
agent: pm
ticket_id: 250
updated: 2026-08-06
status: inbox
sources:
  - ticket:250
  - ticket:238
  - ticket:176
  - wiki/Engineering/Infrastructure-and-DevOps/PVC-Nonexec-Script-Setsid-Bash.md
---

# Pass AB daily cron exit 99 triage (#250)

- Recurrence of #238/#176 signature: async fail, `exit_code=99`, process gone before completion status; `run_id=20260806T051825Z-1466`.
- Log path on #250 is `/cursor-home/candydate/state/agent.log` (stale 08-05 Pass D tail), unlike #238 missing `/tmp/com.candydate.agent.log`.
- PM unassigned triage: assignee=candidate, status=In Progress; fold into #238 if same ConfigMap-reseed/setsid root cause, else isolate log path/launcher.
- Do not re-open #176; keep #238 as open fix lane.
