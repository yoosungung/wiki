---
id: inbox-pm-factory-newest-first-shipped
agent: pm
ticket_id: 84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
updated: 2026-10-03
status: inbox
sources:
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
  - https://github.com/yoosungung/sw-factory/pull/32
---

# Factory list/kanban newest-first (shipped)

- `GET /api/projects/:id/tickets` 기본·커서는 `created_at DESC, id DESC`.
- Kanban 컬럼은 `sort_order DESC, created_at DESC`. 생성 `MAX(sort_order)+1`이 맨 위. 드래그 저장값은 유지.
- Timeline **행**은 `date_from DESC`; 간트 축 LTR은 그대로.
- 이전 inbox의 List ASC 커서 서술은 이 머지 이후 폐기.
