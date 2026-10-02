---
id: inbox-sw-factory-fe-agent-prompt-compose
agent: sw-factory
ticket_id: ba05f9a5-6ba6-4237-8c75-91dbca6774ef
updated: 2026-10-02
status: inbox
sources:
  - ticket:ba05f9a5-6ba6-4237-8c75-91dbca6774ef
  - ARCHITECTURE.md§4
---

# FE Agent prompt compose (F16)

- Tickets 툴바 **Prompt agent** → ticketless `POST /api/agent/prompts`; Issue 헤더/browse는 `ticket_id` 기본값.
- Client: `client.postAgentPrompt` — `ticket_id` null/omit 시 body에서 제외.
- 성공 ack는 `{ id, at }`만; chat/WS/폴링 없음.
- E2E: `e2e/agent-prompt.spec.ts`.
