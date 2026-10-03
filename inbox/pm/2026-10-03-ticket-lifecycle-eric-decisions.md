---
id: inbox-pm-ticket-lifecycle-eric-decisions
agent: pm
ticket_id: 5c9b127e-fe73-4268-85e7-819a14542c0a
updated: 2026-10-03
status: inbox
sources:
  - ticket:5c9b127e-fe73-4268-85e7-819a14542c0a
---

# Factory Done purge 결정 (Eric)

- 28일 물리 삭제 진행. 컷오프는 category=done인 티켓의 `updated_at`.
- 티켓에 연결된 리소스 전부 삭제(comments, files+R2, event log 행 포함).
- 마일스톤 삭제와 일반 티켓 삭제는 독립(자식/부모 연쇄 삭제 없음).
