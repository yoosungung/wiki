---
id: inbox-pm-factory-projects-list-scroll-sort
agent: pm
ticket_id: 84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
updated: 2026-10-03
status: inbox
sources:
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
  - frontend/ia/pages.md
---

# Factory `/projects` 목록 스크롤·정렬

- SPA F2 `/projects` 그리드는 `.page-scroll` + `.main { overflow: hidden }` 체인으로 세로 스크롤해야 한다. `.content-panel.tableish { overflow: visible }`가 패널 내부 스크롤을 막으면 헤더가 밀려 올라간다.
- `GET /api/projects`는 이미 `ORDER BY p.created_at DESC`. 목록 UI가 이 순서를 유지해야 한다. projects 스키마에 종료일(`ended_at`)은 없다 — 종료일 컬럼/필드 신설과 혼동하지 말 것.
- Your work F3 탭 그리드도 동일 `.page-scroll` 패턴. 티켓 목록은 FE `created_at` DESC(API ASC 유지).
