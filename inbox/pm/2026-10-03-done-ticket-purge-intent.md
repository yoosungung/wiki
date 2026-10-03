---
id: inbox-pm-done-ticket-purge-intent
agent: pm
ticket_id: 5c9b127e-fe73-4268-85e7-819a14542c0a
updated: 2026-10-03
status: inbox
sources:
  - ticket:5c9b127e-fe73-4268-85e7-819a14542c0a
  - https://github.com/yoosungung/sw-factory/pull/34
---

# Factory Done ticket 28일 purge

- 컷오프는 `category=done` + `tickets.updated_at`(코멘트는 시계를 안 밈). 7일 archived는 조회 필터, 28일은 hourly Cron 물리 삭제.
- comments/files/pending_uploads/`agent_event_log`는 tickets FK가 없어 purge가 명시 DELETE(+R2)해야 한다. activities/FS deps는 `ON DELETE CASCADE`.
- 마일스톤 행 삭제는 자식 `milestone_id` SET NULL만. 새 archived status 키는 쓰지 않음.
