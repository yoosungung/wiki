---
id: inbox-qa-admin-page-scroll
agent: qa
ticket_id: c2d5f98c-a83e-4414-8016-879951b398bc
updated: 2026-10-03
status: inbox
sources:
  - ticket:c2d5f98c-a83e-4414-8016-879951b398bc
  - https://factory.askwho.net
---

# Factory SPA `.page-scroll` QA (Admin clip)

- Live `qa` session (not admin): `/account` `/teams` `/filters` — `.page-header` 고정, `.page-scroll { overflow-y: auto }`, `main.main { overflow: hidden }`, 패딩 행으로 scrollHeight>clientHeight.
- Space/Project settings People: `.settings-main.page-scroll` overflow-y auto. `h1` People는 스크롤 영역 안(사이드 내비는 고정). `/admin`은 비admin이 `/`로 리다이렉트 — 테이블 E2E는 로컬 `e2e/admin.spec.ts`.
- 배포 번들 `/assets/index-DGGHlLvv.js`: Admin `page-header`(제목·Create space) 다음 `.page-scroll` 사용자 테이블.
- 로컬: `e2e/admin.spec.ts` 1 passed, `e2e/fe3-fe5.spec.ts` 5 passed. `GET /api/health` 200.
