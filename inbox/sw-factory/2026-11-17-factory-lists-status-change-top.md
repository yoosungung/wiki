---
id: inbox-sw-factory-factory-lists-status-change-top
agent: sw-factory
ticket_id: b6ff2c01-481f-44d5-ae9f-e500ee98ae2c
updated: 2026-11-17
status: inbox
sources:
  - ticket:b6ff2c01-481f-44d5-ae9f-e500ee98ae2c
  - wiki/Engineering/AI-Native-Engineering/Factory-Lists-Newest-First.md
---

# Factory Board status-change → column top

- **Board:** create·status 변경 시 서버 `MAX(sort_order)+1`로 컬럼 맨 위. 같은 status DnD만 body `sort_order` 적용. FE `move()`는 sort_order 생략.
- **Backlog·List:** 세로 표시는 `created_at DESC` (`ticketsNewestFirst`). Board `kanbanColumnNewestFirst`와 분리.
- 함정: FE가 `columns[status].length`를 sort_order로 보내면 archived Done 제외·레거시 고값 아래 묻힘 → 서버가 status 변경 시 클라이언트 sort_order 무시.
- canonical `Factory-Lists-Newest-First` Kanban 줄에 “status 변경도 MAX+1” 보강 필요(@km).
