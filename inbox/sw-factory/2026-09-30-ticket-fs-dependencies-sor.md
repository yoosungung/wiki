---
id: inbox-sw-factory-ticket-fs-dependencies-sor
agent: sw-factory
ticket_id: dc1a8800-5609-47b1-b48f-1716695edc96
updated: 2026-09-30
status: inbox
sources:
  - ticket:dc1a8800-5609-47b1-b48f-1716695edc96
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
---

# FS 선행 1급 SoR (sw-factory)

- SoR: D1 `ticket_dependencies(successor_id, blocker_id)` + `GET|PUT /api/tickets/:id/dependencies`.
- Parent는 `milestone_id`만; FS로 쓰면 `400 parent_not_fs`.
- Blocker→`done`: edge clear; 후속 `blocked`이면 `in_progress`; `ticket_updated` + `dependency_cleared`/`unblocked_from` (gateway 전용 타입 없음).
- soft `<!-- blocked-by: -->`: GET dual-read 한 릴리스; PUT/write는 테이블만·마커 strip.
