---
id: inbox-pm-sfa-agent-prompt-ui-howto
agent: pm
ticket_id: dab2382b-0ce2-4efc-9921-5ad8125241c5
updated: 2026-10-02
status: inbox
sources:
  - ticket:dab2382b-0ce2-4efc-9921-5ad8125241c5
  - frontend/ia/pages.md#F16
  - frontend/ia/menus.md
---

# SFA — on-demand Agent prompt UI 사용법

- Project → Tickets(board/backlog/timeline/list) 툴바 **Prompt agent** → Target(멤버 name) + Prompt → **Send**. 티켓 스코프 없음(ticketless wake).
- Issue 사이드패널/`/browse/:id` 헤더 **Prompt agent** → 동일 모달, 현재 이슈 `ticket_id` 자동 포함.
- 성공 시 `Queued event {id} at {at}` ack만 표시. 실시간 chat/응답 대기 UI 없음. 회신은 티켓 코멘트(또는 PVC)로 확인.
- API: `POST /api/agent/prompts` (세션 쿠키). 배포 반영: main `1ed6d25` / PR #25.
