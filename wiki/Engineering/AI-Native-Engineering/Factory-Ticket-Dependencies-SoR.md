---
id: factory-ticket-dependencies-sor
title: "Factory FS 선행 1급 SoR (ticket_dependencies)"
status: canonical
owner: km
updated: "2026-10-02"
review_after: "2027-01-02"
sources:
  - inbox/sw-factory/2026-09-30-ticket-fs-dependencies-sor.md
  - inbox/pm/2026-09-30-fs-deps-intent-pass.md
  - inbox/pm/2026-09-30-ticket-fs-deps-options.md
tags: ["Engineering", "AI-Native", "Factory", "FS"]
type: "wiki"
---

# Factory FS 선행 1급 SoR (ticket_dependencies)

Workers/D1 공장의 Finish-to-Start SoR은 soft HTML 마커가 아니라 **1급 테이블 + REST**다.

## SoR

- 테이블: `ticket_dependencies(successor_id, blocker_id)`
- API: `GET|PUT /api/tickets/:id/dependencies` (`blocker_ids`)
- MCP: `set_blocked_by` → 위 PUT (write는 테이블만)

## Parent vs FS

- Parent/child: **`milestone_id`만**. FS로 쓰면 `400 parent_not_fs`.
- Leantime 시대 `dependingTicketId` / soft `<!-- blocked-by: -->` 혼동 금지. 레거시 대비: [[wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md]]

## Unblock

- Blocker → `done`: edge clear.
- 후속이 `blocked`이고 남은 blocker가 없으면 복귀 status = **`in_progress`** (스냅샷 컬럼 없음).
- Wake: 전용 `event_type` 없음 — `ticket_updated` + `dependency_cleared` / `unblocked_from`.
- soft 마커: GET dual-read는 한 릴리스 과도기; PUT/write는 테이블만·마커 strip.
