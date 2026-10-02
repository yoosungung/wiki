---
id: inbox-sw-factory-post-agent-prompts-manual-prompt
agent: sw-factory
ticket_id: d9d06c0a-d068-4133-96bd-0e565dc3a6ff
updated: 2026-10-02
status: inbox
sources:
  - ticket:d9d06c0a-d068-4133-96bd-0e565dc3a6ff
  - ARCHITECTURE.md§4-Agent-outbox
---

# POST /api/agent/prompts → manual_prompt

- 세션 쿠키 POST `{ project_id, target, prompt, ticket_id? }` → `agent_event_log` `event_type=manual_prompt`, 응답 `{ id, at }` (201).
- target: `users.name` 대소문자무시 exact 우선, 아니면 UUID; 호출자·target 모두 project_members.
- ticket_id는 같은 project 소속이어야 함; 실패 코드 `invalid_body`/`invalid_target`/`invalid_ticket`/403.
