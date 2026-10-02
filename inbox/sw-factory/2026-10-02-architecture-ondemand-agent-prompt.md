---
id: inbox-sw-factory-architecture-ondemand-agent-prompt
agent: sw-factory
ticket_id: 5207c068-3554-4a82-acec-ef6685b093af
updated: 2026-10-02
status: inbox
sources:
  - ticket:5207c068-3554-4a82-acec-ef6685b093af
  - ticket:24d399f1-9f7d-43c2-912b-9092834c6227
  - ARCHITECTURE.md§1#11§Agent-outbox
---

# ARCHITECTURE on-demand agent prompt (Option A)

- Wake outbox 출처: 티켓 mutate + `POST /api/agent/prompts` → `event_type=manual_prompt` (push 금지).
- target: `users.name` 우선(agents.yaml 대응) 또는 user UUID; 호출자·target 모두 project_members.
- `ticket_id` optional — 있으면 Active MCP 스코프; 없으면 티켓리스, 회신 SoR 없음(PVC/gateway 로그만).
