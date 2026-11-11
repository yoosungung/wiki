---
id: inbox-pm-ticket-picker-intent-pass
agent: pm
ticket_id: 35557b59-f071-4c75-a598-0d9d29a0d7bc
updated: 2026-11-11
status: inbox
sources:
  - ticket:35557b59-f071-4c75-a598-0d9d29a0d7bc
  - https://github.com/yoosungung/sw-factory/pull/46
  - wiki/Engineering/AI-Native-Engineering/Factory-Issue-Details-Parent-Children.md
---

# Issue Details TicketPicker Intent Pass

- SPA Parent / Blocked by / Children 기존 연결은 인라인 `TicketPicker`(7d + `exclude_done` 콤보, UUID paste, `/api/search` typeahead)로 충분. 계약 축은 Parent=`milestone_id`, Blocked by=`dependencies` 분리 유지.
- Children 기존 티켓 연결은 `getTicket` → 그 `version`으로 `PATCH milestone_id`(OCC). 공용 컴포넌트 추출은 재사용 2곳 이상일 때만.
- 이 repo는 PR 브랜치 Test workflow가 main에 없고 Deploy만 main push — Intent는 로컬 vitest + diff AC 매핑으로 판정 가능.
