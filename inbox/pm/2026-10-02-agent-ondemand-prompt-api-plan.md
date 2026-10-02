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

- Eric 승인: Option A — Worker POST /api/agent/prompts → agent_event_log → gateway deliverTicketless (#1·#11 유지).
- 회신 SoR: fire-and-forget. ticket_id 있으면 티켓 MCP; 없으면 PVC/gateway 로그. chat 테이블 없음.
- target: name 우선(+user_id). 권한: 세션·project member.
- Follow-ups: docs 66cd23e9… → BE 4ffe8048… → gateway e51ad197…
