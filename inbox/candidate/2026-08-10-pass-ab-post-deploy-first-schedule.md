---
id: inbox-candidate-pass-ab-post-deploy-first-schedule
agent: candidate
ticket_id: 308
updated: 2026-08-10
status: inbox
sources:
  - ticket:308
  - ticket:430
---

# Pass AB post-deploy first schedule — PASS

- Eric thin-shim deploy 이후 첫 `candydate-pass-ab-launch` (`0 12 * * *`, 2026-08-10T03:00Z) 관찰 완료.
- Job `candydate-pass-ab-launch-29772180` Complete; CronJob suspend=False.
- `state.env`: run_id=`20260810T030001Z-3770`, status=`done`, exit_code=`0` (03:00:01Z–03:14:58Z).
- `worker.log`: start + finishing 둘 다 기록 (공백/exit 99 아님).
- PVC skill launchers remain thin shim (`exec bash …/agent/cron/…`, ~131B, nohup 없음).
- Leantime cron report #430 Done; #308 재오픈 불필요.
