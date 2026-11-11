---
id: factory-ticketpicker-7d-combo
title: "Factory SPA TicketPicker (7d · exclude_done)"
status: canonical
owner: km
updated: "2026-11-12"
last_updated: "2026-11-12"
review_after: "2027-02-12"
sources:
  - inbox/pm/2026-11-11-issue-ticket-picker-combo.md
  - inbox/pm/2026-11-11-ticket-picker-intent-pass.md
  - inbox/pm/2026-11-11-pm-checkpoint-ticket-picker-done.md
  - inbox/sw-factory/2026-11-11-issue-ticket-picker-combo.md
  - ticket:35557b59-f071-4c75-a598-0d9d29a0d7bc
  - wiki/Engineering/AI-Native-Engineering/Factory-Issue-Details-Parent-Children.md
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
tags: ["Engineering", "AI-Native", "Factory", "SPA"]
type: wiki
---

# Factory SPA TicketPicker (7d · exclude_done)

Parent / Blocked by / Children 연결의 UUID 수동 입력 병목을 줄인다. MCP·agent는 id 계약 유지 — **SPA UX만**.

## 동작

| 축 | 계약 |
| :--- | :--- |
| 목록 | `exclude_done` + client **7일** `created_at` 콤보 |
| 폴백 | UUID paste; miss 시 같은 project `/api/search` typeahead |
| Children 기존 연결 | `getTicket` → 그 `version`으로 `PATCH milestone_id` (OCC) |
| 축 분리 | Parent=`milestone_id` ≠ FS `ticket_dependencies` |

공용 컴포넌트 추출은 재사용 2곳 이상일 때만. 이 repo PR 브랜치 Test workflow가 main에 없으면 Intent는 로컬 vitest + diff AC로 판정 가능(Deploy만 main push).

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Factory-Issue-Details-Parent-Children.md]]
- [[wiki/Engineering/AI-Native-Engineering/Factory-Parent-Milestone-Not-Start-Gate.md]]
