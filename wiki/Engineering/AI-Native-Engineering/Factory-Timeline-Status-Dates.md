---
id: factory-timeline-status-dates
title: "Factory Timeline: status-derived date_from/date_to"
status: canonical
owner: km
updated: "2026-10-02"
review_after: "2027-01-02"
sources:
  - inbox/pm/2026-09-30-factory-timeline-status-dates.md
  - inbox/pm/2026-09-30-timeline-status-dates.md
  - inbox/sw-factory/2026-09-30-timeline-status-dates.md
tags: ["Engineering", "AI-Native", "Factory", "Timeline"]
type: "wiki"
---

# Factory Timeline: status-derived date_from/date_to

`GET /api/projects/:id/timeline`는 저장된 `date_from`·`date_to`가 **둘 다 NOT NULL**인 ticket/milestone만 반환한다. 대부분 작업 티켓이 두 필드를 비워 두면 Timeline이 비어 보인다.

## 규칙

- **자동 채움 기본 경로**: backlog(또는 생성) 진입 ≈ 시작(`date_from`), 첫 `done` 진입 ≈ 종료(`date_to`). UTC `YYYY-MM-DD`.
- **수동 기간 override**: create/PATCH에 문자열로 준 값은 유지. SPA가 `null`을 보내던 Create는 null/empty를 omitted으로 취급해 auto-fill을 막지 않는다.
- **첫 done**: `date_to`가 아직 `created_at` 날짜(자동 open bar)와 같을 때만 교체.
- **기존 행**: migration `0007_timeline_status_dates` (activity history → 없으면 created_at / done updated_at / today).
- **조회 API만으로 필드 없이 보이게 바꾸지 않음** — 타임라인 계약(§6)과 어긋난다.

L0 계약 본문은 복제하지 않는다. 구현 SoR은 sw-factory `ARCHITECTURE` / timeline 라우트.
