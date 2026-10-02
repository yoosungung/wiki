---
id: inbox-sw-factory-fe-agent-prompt-compose
agent: sw-factory
ticket_id: dab2382b-0ce2-4efc-9921-5ad8125241c5
updated: 2026-10-02
status: inbox
sources:
  - ticket:dab2382b-0ce2-4efc-9921-5ad8125241c5
  - frontend/ia/pages.md#F16
---

# FE Agent prompt compose (F16)

- Tickets 툴바·Issue 헤더 **Prompt agent** 모달 → `POST /api/agent/prompts` (세션 쿠키).
- body `{ project_id, target, prompt, ticket_id? }`; 성공 ack `{ id, at }`; 응답 대기/chat UI 없음.
- target = project member `name`; Issue에서 열면 `ticket_id` 기본, 툴바면 omit.
