---
id: inbox-sw-factory-manual-prompt-contract
agent: sw-factory
ticket_id: 2996efbf-b991-46b2-aba1-42940e4d06ea
updated: 2026-10-02
status: inbox
sources:
  - ticket:2996efbf-b991-46b2-aba1-42940e4d06ea
  - ticket:24d399f1-9f7d-43c2-912b-9092834c6227
  - ARCHITECTURE.md§1#11§4
---

# manual_prompt on-demand wake (Option A)

- Eric 승인 Option A: `POST /api/agent/prompts` → `agent_event_log` `event_type=manual_prompt` → gateway `deliverTicketless` (코드 후속).
- target: `users.name` 우선 또는 UUID; 호출자·target 모두 project member; 세션 쿠키만.
- `ticket_id` optional — 있으면 Active MCP 스코프, 없으면 티켓리스(회신 SoR = PVC/로그, chat 테이블 없음).
