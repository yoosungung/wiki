---
id: inbox-sw-factory-backlog-timeline-page-scroll
agent: sw-factory
ticket_id: 8d8acba4-c49a-421a-9255-5bafd72f8706
updated: 2026-10-04
status: inbox
sources:
  - ticket:8d8acba4-c49a-421a-9255-5bafd72f8706
  - wiki/Engineering/AI-Native-Engineering/Factory-SPA-Page-Scroll.md
---

# Backlog/Timeline `.page-scroll` 적용

- Tickets `?view=backlog`·`?view=timeline`도 List와 같이 툴바 고정 + 본문 `.page-scroll` (`.main { overflow: hidden }` 유지).
- `.backlog-panel`/`content-panel` overflow만으로는 클리핑 해결 안 됨 — 뷰 전체 본문을 스크롤포트로 감싼다.
- 단위: `ProjectWorkspace.page-scroll.test.tsx`; e2e: `projects-newest.spec.ts` Backlog/Timeline pad-scroll.
