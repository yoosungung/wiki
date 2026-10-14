---
id: factory-timeline-list-row-4col
title: "Factory Timeline: list-row 4열 vs 공유 3열"
status: canonical
owner: km
updated: "2026-10-15"
review_after: "2027-01-15"
sources:
  - inbox/pm/2026-10-15-timeline-list-row-4cell-3col.md
  - inbox/sw-factory/2026-10-15-timeline-list-timeline-4col.md
  - ticket:54683314-7fe6-4d5d-8a13-f19985b89505
  - https://github.com/yoosungung/sw-factory/pull/40
  - wiki/Engineering/AI-Native-Engineering/Factory-Timeline-Status-Dates.md
tags: ["Engineering", "AI-Native", "Factory", "Timeline", "CSS"]
type: "wiki"
---

# Factory Timeline: list-row 4열 vs 공유 3열

Timeline 행은 date | issue-key | title | status (**4 children**)인데 공유 `.list-row`는 `grid-template-columns: 160px 1fr 120px` (**3열**)이라 key가 `1fr`을 먹고 title이 120px에 갇히며 status가 줄바꿈된다.

## 고침 패턴

- 공유 `.list-row`는 clients/기타 목록용 **3열** 유지: `160px 1fr 120px`.
- Timeline만 `.list-row.list-timeline` → `auto minmax(0,10rem) minmax(0,1fr) auto` (title이 넓은 열, status 한 줄, >768px).
- Mobile `<768px`: `.list-row.list-timeline`도 기본 `.list-row`처럼 `1fr` 스택.

날짜 자동채움 계약은 [[wiki/Engineering/AI-Native-Engineering/Factory-Timeline-Status-Dates.md]]. L0 CSS/컴포넌트 본문은 복제하지 않는다.
