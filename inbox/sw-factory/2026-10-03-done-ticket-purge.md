---
id: inbox-sw-factory-done-ticket-purge
agent: sw-factory
ticket_id: 5c9b127e-fe73-4268-85e7-819a14542c0a
updated: 2026-10-03
status: inbox
sources:
  - ticket:5c9b127e-fe73-4268-85e7-819a14542c0a
  - ARCHITECTURE.md§6
---

# Factory Done 28일 purge

- 7일 archived Done은 조회 필터(`DONE_ARCHIVE_DAYS`). 28일 물리 삭제는 hourly Cron + `DONE_PURGE_DAYS=28`.
- 컷오프는 `category=done`인 행의 `tickets.updated_at`. 코멘트 INSERT는 이 시계를 밀지 않는다.
- comments/files는 tickets FK가 없어 purge가 R2 키와 함께 명시 DELETE. `ticket_activities`/`ticket_dependencies`는 ticket DELETE CASCADE.
- 마일스톤 purge는 자식 `milestone_id` SET NULL만. 태스크 purge는 부모 마일스톤을 지우지 않음.
