---
id: factory-timeline-merged-into-list
title: "Factory Timeline 세그먼트 → List 통합 (Option B)"
status: canonical
owner: km
updated: "2026-11-17"
last_updated: "2026-11-17"
review_after: "2027-02-17"
sources:
  - inbox/pm/2026-11-16-timeline-vs-list-merge.md
  - inbox/sw-factory/2026-11-16-timeline-merged-into-list.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Timeline-List-Row-4col.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Timeline-Status-Dates.md
tags: ["Engineering", "Factory", "SPA", "Timeline", "List"]
type: wiki
---

# Factory Timeline 세그먼트 → List 통합 (Option B)

Tickets 툴바는 **`Board|Backlog|List`** 만. Timeline 탭 제거 (F7 간트+행 vs F8 테이블 행 UX 중복; status-derived `date_from`/`date_to` 이후 Timeline 행이 거의 전부 채워져 중복 체감↑).

## SPA 계약

- 레거시 `?view=timeline` deep link → List (`parseViewMode`).
- List Due 셀: `due_at` 우선, 없으면 `date_from → date_to`.
- `GET /api/projects/:id/timeline`은 당분간 호환 유지; SPA는 호출하지 않음 (API deprecate는 ARCHITECTURE 서브태스크).

## 비선택

- 캘린더 전환(옵션 C)은 별도 큰 범위 — 이 페이지 범위 밖.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Factory-Timeline-List-Row-4col.md]] (레거시 4열 CSS — Timeline 탭 제거 후에도 list-row 참고)
- [[wiki/Engineering/AI-Native-Engineering/Factory-Timeline-Status-Dates.md]]
