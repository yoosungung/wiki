---
id: inbox-pm-agent-ondemand-prompt-api-plan
agent: pm
ticket_id: 24d399f1-9f7d-43c2-912b-9092834c6227
updated: 2026-10-02
status: inbox
sources:
  - ticket:24d399f1-9f7d-43c2-912b-9092834c6227
  - deploy/docs/schedules.md
  - ARCHITECTURE.md§1#1#11#12
---

# Agent on-demand prompt API (schedule-shaped)

- 현 wake는 티켓 이벤트 · gateway `schedules[]` · 기동 catch-up 세 종류뿐. Worker 공개 write API 없음.
- 스케줄형 온디맨드 = persona+prompt → `deliverTicketless`(기본 티켓리스). 권고: Worker `POST /api/agent/prompts` → `agent_event_log` → gateway pull (#1·#11 유지).
- gateway 로컬 HTTP는 SPA 불가(#1). `@mention`만으로는 freeform 온디맨드와 다름.
- 열린 결정: 회신 SoR(티켓 강제 vs PVC vs chat 테이블), target 키(user_id vs name/lane), 호출 권한.
