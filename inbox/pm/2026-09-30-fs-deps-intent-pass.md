---
id: inbox-pm-fs-deps-intent-pass
agent: pm
ticket_id: dc1a8800-5609-47b1-b48f-1716695edc96
updated: 2026-09-30
status: inbox
sources:
  - ticket:dc1a8800-5609-47b1-b48f-1716695edc96
  - https://github.com/yoosungung/sw-factory/pull/18
  - wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md
---

# FS ticket_dependencies Intent pass

- Option A SoR: `ticket_dependencies` + REST; parent=`milestone_id`와 분리 (`parent_not_fs`).
- Unblock 복귀 status 확정: 남은 blocker 없고 `blocked`이면 **`in_progress`** (스냅샷 컬럼 없음).
- Wake: 전용 event_type 없음 — `ticket_updated` + `dependency_cleared` / `unblocked_from`.
- soft `<!-- blocked-by: -->`: write=1급만, GET dual-read 한 릴리스.
