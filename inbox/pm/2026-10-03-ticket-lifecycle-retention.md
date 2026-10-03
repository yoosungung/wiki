---
id: inbox-pm-ticket-lifecycle-retention
agent: pm
ticket_id: 5c9b127e-fe73-4268-85e7-819a14542c0a
updated: 2026-10-03
status: inbox
sources:
  - ticket:5c9b127e-fe73-4268-85e7-819a14542c0a
  - ARCHITECTURE.md§6
---

# Factory Done 티켓 수명주기

- 7일 archived Done은 **별도 status가 아님**. `category=done` + `updated_at` 조회 필터(`DONE_ARCHIVE_DAYS=7`, `include_archived=true`).
- 28일 D1 물리 삭제는 2026-10-03 시점 **미구현**. 자동 purge는 수동 삭제 가드(작성자/owner)와 충돌하므로 Eric 승인 게이트.
- `comments`/`files`는 `tickets(id)` FK가 없어 ticket DELETE만 하면 고아 행이 남는다. purge 시 명시 삭제 + R2 객체 정리 필요.
- archive/purge 시계가 `updated_at`이면 done 이후 패치가 컷오프를 밀어낸다.
