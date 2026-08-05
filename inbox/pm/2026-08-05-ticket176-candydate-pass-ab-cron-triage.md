---
id: inbox-pm-ticket176-candydate-pass-ab-cron-triage
agent: pm
ticket_id: 176
updated: 2026-08-05
status: inbox
sources:
  - ticket:176
  - leantime:project:7:candidate.win
---

# Candydate Pass AB cron 실패 triage

- Unassigned cron 실패 티켓(`cursorbridge-unassigned-triage`)은 project `candidate.win` Pass AB/D 작업의 owner를 **candidate**(Leantime user id 9)로 배정한다.
- exit_code 99 + “process disappeared before writing completion status” + `/tmp/com.candydate.agent.log` missing → agent-actionable 진단(재시작/OOM/timeout/로그 경로). human-only Approval이 아님.
- PM 조치: status `In Progress`, `@candidate` 멘션, 30m checkpoint(원인 1줄 + 재실행/PR/blocker).
