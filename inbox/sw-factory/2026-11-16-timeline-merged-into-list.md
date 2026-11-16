---
id: inbox-sw-factory-timeline-merged-into-list
agent: sw-factory
ticket_id: ec2d5fbd-6892-4b12-844b-54b5fbc71e2c
updated: 2026-11-16
status: inbox
sources:
  - ticket:ec2d5fbd-6892-4b12-844b-54b5fbc71e2c
  - wiki/Engineering/AI-Native-Engineering/Factory-Timeline-List-Row-4col.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Timeline-Status-Dates.md
---

# Timeline 세그먼트 → List 통합 (Option B)

- Tickets 툴바는 `Board|Backlog|List`만. Timeline 탭 제거.
- 레거시 `?view=timeline` deep link → List (`parseViewMode`).
- List Due 셀: `due_at` 우선, 없으면 `date_from → date_to`.
- `GET /api/projects/:id/timeline`은 당분간 호환 유지; SPA는 더 이상 호출하지 않음.
- 간트/기간 드래그·캘린더 뷰는 Non-goal (별 옵션).
- 기존 Timeline 4-col CSS(`.list-timeline`)·status-derived dates wiki는 역사 참고; List Due가 일정 표기 SoR.
