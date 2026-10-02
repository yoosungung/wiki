---
id: factory-on-demand-agent-prompt
title: "Factory on-demand agent prompt (manual_prompt / Option A)"
status: canonical
owner: km
updated: "2026-10-03"
review_after: "2027-01-03"
sources:
  - inbox/pm/2026-10-02-agent-ondemand-prompt-api-plan.md
  - inbox/pm/2026-10-02-option-a-duplicate-cleanup.md
  - inbox/pm/2026-10-02-fe-agent-prompt-ui.md
  - inbox/pm/2026-10-02-sfa-agent-prompt-ui-howto.md
  - inbox/sw-factory/2026-10-02-architecture-ondemand-agent-prompt.md
  - inbox/sw-factory/2026-10-02-manual-prompt-contract.md
  - inbox/sw-factory/2026-10-02-post-agent-prompts-manual-prompt.md
  - inbox/sw-factory/2026-10-02-fe-agent-prompt-compose.md
  - ticket:24d399f1-9f7d-43c2-912b-9092834c6227
  - ticket:5207c068-3554-4a82-acec-ef6685b093af
  - https://github.com/yoosungung/sw-factory/pull/21
  - https://github.com/yoosungung/sw-factory/pull/25
tags: ["Engineering", "AI-Native", "Factory", "Gateway"]
type: "wiki"
---

# Factory on-demand agent prompt (manual_prompt / Option A)

## 계약

- Eric 승인 Option A: `POST /api/agent/prompts` → `agent_event_log` `event_type=manual_prompt` → gateway `deliverTicketless` (push wake 금지 유지).
- Body: `{ project_id, target, prompt, ticket_id? }` → 201 `{ id, at }`.
- `target`: `users.name` 대소문자무시 exact 우선, 아니면 UUID. 호출자·target 모두 `project_members`.
- `ticket_id` optional: 있으면 Active MCP 스코프; 없으면 티켓리스(회신 SoR = PVC/gateway 로그, **chat 테이블·WS 없음**).
- 실패 코드: `invalid_body` / `invalid_target` / `invalid_ticket` / 403.

## UI (F16)

- Tickets 툴바 **Prompt agent** → ticketless wake.
- Issue 사이드패널 / `/browse/:id` → 현재 `ticket_id` 자동 포함.
- Ack만 표시; 실시간 응답 UI 없음. 회신은 티켓 코멘트(또는 PVC).
- Client: `postAgentPrompt` — null `ticket_id`는 body에서 제외. E2E: `e2e/agent-prompt.spec.ts`.

## Ops 함정

- docs/BE/gateway 티켓 fan-out 시 **정본 1줄**만 유지; sibling merge 후 빈 “정본” 슬롯은 superseded-close해야 FS unblock.
- 배포 예: ARCHITECTURE merge PR #21; UI main `1ed6d25` / PR #25.
