---
id: factory-lists-newest-first
title: "Factory 목록/칸반 newest-first"
status: canonical
owner: km
updated: "2026-11-17"
review_after: "2027-02-17"
sources:
  - inbox/pm/2026-10-03-factory-ticket-views-newest-first.md
  - inbox/pm/2026-10-03-factory-newest-first-shipped.md
  - inbox/pm/2026-10-03-factory-projects-list-scroll-sort.md
  - inbox/sw-factory/2026-10-03-factory-ticket-views-newest-first.md
  - inbox/qa/2026-10-03-factory-newest-first-qa-pass.md
  - inbox/aa/2026-10-03-factory-newest-first-security-pass.md
  - inbox/ta/2026-10-03-factory-newest-first-prod.md
  - inbox/sw-factory/2026-11-17-factory-lists-status-change-top.md
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
  - ticket:b6ff2c01-481f-44d5-ae9f-e500ee98ae2c
  - https://github.com/yoosungung/sw-factory/pull/32
  - https://github.com/yoosungung/sw-factory/pull/56
tags: ["Engineering", "AI-Native", "Factory", "API", "SPA"]
type: "wiki"
---

# Factory 목록/칸반 newest-first

## API·표시 (shipped)

| 표면 | 정렬 |
| --- | --- |
| `GET /api/projects/:id/tickets` (List) | `created_at DESC, id DESC` (커서 동일 방향) |
| Backlog 세로 | `created_at DESC` (`ticketsNewestFirst`) — Board `sort_order`와 분리 |
| Board(Kanban) 컬럼 | `sort_order DESC, created_at DESC` |
| Board create·**status 변경** | 서버 `MAX(sort_order)+1` → 해당 컬럼 **맨 위**. 같은 status DnD만 body `sort_order` 적용 |
| `GET /api/projects` | `created_at DESC` (+ `id DESC` tie-break) |
| Your work Assigned/Created·댓글 | FE `created_at` DESC |

Timeline 탭은 List로 통합됨 — [[wiki/Engineering/AI-Native-Engineering/Factory-Timeline-Merged-Into-List.md]].

## 함정

- List API를 ASC로 두고 FE에서 한 페이지만 뒤집으면 최신 티켓이 **다음 페이지**에 남는다 → API 방향과 커서를 같이 뒤집는다.
- FE `move()`가 `columns[status].length`를 `sort_order`로 보내면 archived Done 제외·레거시 고값 아래 묻힘 → **status 변경 시 서버가 클라이언트 `sort_order` 무시**, `MAX+1`만 사용.
- Backlog를 `kanbanColumnNewestFirst`(`sort_order`)로 그리면 옛 고값 카드가 위에 남음 → **생성일 순**으로 그릴 것.
- projects 스키마에 `ended_at` 없음 — 종료일 컬럼 신설과 혼동 금지.
- 커서 opaque `{created_at,id}`; 방향만 DESC, invalid cursor는 400.

## 검증

- QA live (PR #56): Board status 이동 시 맨 위; Backlog·List 생성일 최신 위.
- AA: ORDER BY/커서·FE sort helpers만 — membership/session/admin 표면 불변.
- Prod CD: [[wiki/Engineering/Infrastructure-and-DevOps/Factory-Workers-Single-Env-CD.md]].
