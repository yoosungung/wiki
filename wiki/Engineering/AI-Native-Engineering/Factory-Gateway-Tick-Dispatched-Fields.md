---
id: factory-gateway-tick-dispatched-fields
title: "Gateway tick dispatched: ticket_id · ticket_no · agent_id"
status: canonical
owner: km
updated: "2026-10-02"
review_after: "2027-01-02"
sources:
  - inbox/pm/2026-09-30-gateway-tick-dispatched-fields.md
  - inbox/sw-factory/2026-09-30-gateway-tick-dispatched-ticket-id.md
  - inbox/sw-factory/2026-09-30-gateway-tick-ticket-no.md
tags: ["Engineering", "AI-Native", "Factory", "Gateway"]
type: "wiki"
---

# Gateway tick dispatched fields

`cli.ts`가 processed 또는 dispatched가 비어 있지 않을 stdout에 `{ msg: "tick", processed, acked_id, dispatched }`를 남긴다.

## `dispatched[]` 항목

| 필드 | 의미 |
|------|------|
| `event_id` | agent event UUID |
| `persona` | persona 이름 |
| `agent_id` | Cursor sticky session id |
| `ticket_id` | 이벤트 티켓 UUID (없으면 null) |
| `ticket_no` | UI `issueKey(project.name, ticket.id)` — 예: `SWF-EA2D` (순번 아님, raw UUID 단독 아님) |

`ticket_no` prefix는 프로젝트 이름이 필요하므로 gateway가 `GET /api/projects/:id`를 캐시한다. Worker REST/스키마 변경 없음 — TickResult 관측성만.
