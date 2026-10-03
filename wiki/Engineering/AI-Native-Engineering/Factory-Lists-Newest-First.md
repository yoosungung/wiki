---
id: factory-lists-newest-first
title: "Factory 목록/칸반/타임라인 newest-first"
status: canonical
owner: km
updated: "2026-10-04"
review_after: "2027-01-04"
sources:
  - inbox/pm/2026-10-03-factory-ticket-views-newest-first.md
  - inbox/pm/2026-10-03-factory-newest-first-shipped.md
  - inbox/pm/2026-10-03-factory-projects-list-scroll-sort.md
  - inbox/sw-factory/2026-10-03-factory-ticket-views-newest-first.md
  - inbox/qa/2026-10-03-factory-newest-first-qa-pass.md
  - inbox/aa/2026-10-03-factory-newest-first-security-pass.md
  - inbox/ta/2026-10-03-factory-newest-first-prod.md
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
  - https://github.com/yoosungung/sw-factory/pull/32
tags: ["Engineering", "AI-Native", "Factory", "API", "SPA"]
type: "wiki"
---

# Factory 목록/칸반/타임라인 newest-first

## API·표시 (shipped)

| 표면 | 정렬 |
| --- | --- |
| `GET /api/projects/:id/tickets` | `created_at DESC, id DESC` (커서 동일 방향) |
| Kanban 컬럼 | `sort_order DESC, created_at DESC` — 생성 `MAX(sort_order)+1`이 맨 위; 드래그 저장값 유지 |
| Timeline **행** | `date_from DESC`; 간트 축 LTR(과거→미래)은 유지 |
| `GET /api/projects` | 이미 `created_at DESC` (+ `id DESC` tie-break) |
| Your work Assigned/Created·댓글 | FE `created_at` DESC |

## 함정 (머지 전 서술 폐기)

- List API를 ASC로 두고 FE에서 한 페이지만 뒤집으면 최신 티켓이 **다음 페이지**에 남는다 → API 방향과 커서를 같이 뒤집는다.
- projects 스키마에 `ended_at` 없음 — 종료일 컬럼 신설과 혼동 금지.
- 커서 opaque `{created_at,id}`; 방향만 DESC, invalid cursor는 400.

## 검증

- QA live: projects UniTutorAI→CrewRP→sw-factory; tickets/kanban/timeline DESC; `/projects` 헤더 고정 + `.page-scroll`.
- AA: ORDER BY/커서·FE sort helpers만 — membership/session/admin 표면 불변.
- Prod CD: [[wiki/Engineering/Infrastructure-and-DevOps/Factory-Workers-Single-Env-CD.md]] (descendant SHA 재사용).
