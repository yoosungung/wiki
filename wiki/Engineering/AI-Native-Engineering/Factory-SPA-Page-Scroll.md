---
id: factory-spa-page-scroll
title: "Factory SPA: `.main` overflow + `.page-scroll` 스크롤포트"
status: canonical
owner: km
updated: "2026-10-05"
review_after: "2027-01-04"
sources:
  - inbox/pm/2026-10-03-admin-page-scroll.md
  - inbox/pm/2026-10-03-factory-projects-list-scroll-sort.md
  - inbox/sw-factory/2026-10-03-admin-page-scroll.md
  - inbox/sw-factory/2026-10-03-spa-list-page-scroll.md
  - inbox/qa/2026-10-03-admin-page-scroll-qa.md
  - inbox/aa/2026-10-03-admin-page-scroll-security-pass.md
  - inbox/aa/2026-10-03-spa-list-page-scroll-security-pass.md
  - ticket:c2d5f98c-a83e-4414-8016-879951b398bc
  - ticket:900893c0-b570-496c-859a-ce201e3b57bc
  - https://github.com/yoosungung/sw-factory/pull/28
  - https://github.com/yoosungung/sw-factory/pull/31
  - inbox/pm/2026-10-04-backlog-timeline-page-scroll-gap.md
  - inbox/sw-factory/2026-10-04-backlog-timeline-page-scroll.md
  - ticket:8d8acba4-c49a-421a-9255-5bafd72f8706
tags: ["Engineering", "AI-Native", "Factory", "SPA", "CSS"]
type: "wiki"
---

# Factory SPA: `.main` overflow + `.page-scroll` 스크롤포트

## 문제

`.main { overflow: hidden; min-height: 0 }` + flex column이면, 콘텐츠가 `.page-scroll`(flex 1, overflow-y auto)로 감싸이지 않을 때 **본문 스크롤이 없고 잘린다**. body 스크롤로 우회하지 않는다. `.main { overflow: visible }`는 보드 컬럼 레이아웃을 깨므로 금지.

## 패턴

1. 크롬(사이드바·탭)·`.page-header`는 스크롤 밖에 둔다.
2. 긴 목록/테이블만 `.page-scroll`에 넣는다 (`flex: 1; min-height: 0; overflow-y: auto`).
3. Nested flex: 스크롤 자식에 `min-height: 0`.
4. Settings People: `.settings-main.page-scroll` (`.main > .settings-layout`가 높이를 채움).
5. `.content-panel.tableish { overflow: visible }`만으로는 `.main` 클리핑을 못 푼다 — 스크롤포트가 필요.

## 적용 표면 (2026-10-03)

| 경로 | 메모 |
| --- | --- |
| `/admin` | 사용자 테이블은 `.page-scroll`; Create space는 `.page-header` |
| `/account` `/teams` `/filters` | Your work와 동일 패턴 |
| Space/Project settings People | `.settings-main.page-scroll` |
| `/projects` | 그리드가 `.page-scroll`을 소유; 헤더 고정 |
| Search | 이미 `.page-scroll` |
| Tickets `?view=backlog` | 툴바 고정 + 본문 `.page-scroll` (2026-10-04) |
| Tickets `?view=timeline` | 동일; `.backlog-panel`/`content-panel` overflow만으로는 클리핑 미해결 |

## 게이트

- AA: layout/CSS만 → trust boundary 아님. sw-factory에 `.factory/quality.yaml` 없으면 `security.command` mechanical skip([[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]).
- QA: live overflow 체인 + 로컬 `e2e/admin.spec.ts` / list scroll specs. `/admin` 테이블 E2E는 admin 세션 필요(비admin은 `/` 리다이렉트).
