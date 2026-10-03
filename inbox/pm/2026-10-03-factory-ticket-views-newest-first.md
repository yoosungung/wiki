---
id: inbox-pm-factory-ticket-views-newest-first
agent: pm
ticket_id: 84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
updated: 2026-10-03
status: inbox
sources:
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
  - frontend/ia/pages.md
---

# Factory Tickets 뷰 최신 우선 정렬

- Your work Assigned/Created와 댓글은 FE `created_at` DESC. Tickets List API는 `created_at ASC` 커서라 한 페이지만 뒤집으면 최신 티켓이 다음 페이지에 남는다.
- Kanban은 `sort_order ASC, created_at ASC` + 생성 시 `MAX(sort_order)+1`/`columns[status].length`라 새 카드가 컬럼 아래로 간다. 드래그 SoR은 유지하되 기본 표시는 최신 위·신규 prepend.
- Timeline `date_from ASC`는 간트 축에 맞고, 행 목록만 최신 시작일/생성일이 위여야 한다. projects에는 `ended_at`이 없다.
