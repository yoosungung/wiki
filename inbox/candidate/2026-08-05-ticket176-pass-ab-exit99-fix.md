---
id: inbox-candidate-ticket176-pass-ab-exit99-fix
agent: candidate
ticket_id: 176
updated: 2026-08-05
status: inbox
sources:
  - ticket:176
  - inbox/pm/2026-08-05-ticket176-candydate-pass-ab-cron-triage.md
---

# Pass AB exit 99 — 0644 exec + /tmp log

- `candydate_pass_ab_launcher.sh`가 `exec "$WORKER"`로 PVC 시드 스크립트(mode 0644, no +x)를 직접 exec → Permission denied → completion status 미기록 → monitor `exit_code=99`.
- 수정: `setsid` + `exec bash "$@"`; 로그 기본 경로 `/cursor-home/candydate/state/agent.log` (export `CANDYDATE_LOG_FILE`).
- Pod/CronJob 재시작·OOM 없음(RESTARTS=0). exit 99 재현·수정 후 재실행은 `exit_code=1` + 영속 로그 기록.
- 후속 blocker: `agent/.env`에 `OPENAI_API_KEY` 없음 → `deep_agent.py` orchestrator(`openai:gpt-5.4-mini`) 즉시 실패.
