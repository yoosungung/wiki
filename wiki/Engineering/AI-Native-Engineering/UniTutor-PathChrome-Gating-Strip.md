---
id: unitutor-pathchrome-gating-strip
title: "UniTutor PathChrome: 접힘 기본 · 로컬 expanded · CF single-env gate"
status: canonical
owner: km
updated: "2026-10-13"
review_after: "2027-01-13"
sources:
  - inbox/pm/2026-10-12-path-chrome-gating-strip-intent-pass.md
  - inbox/uni-tutor/2026-10-12-path-chrome-gating-strip.md
  - inbox/ta/2026-10-12-unitutor-path-chrome-test-deploy.md
  - inbox/qa/2026-10-12-unitutor-path-chrome-qa-smoke.md
  - inbox/ta/2026-10-12-unitutor-path-chrome-prod-gate.md
  - ticket:793c7592-3071-4ab1-a07b-f96a9ee8703c
  - https://github.com/yoosungung/UniTutorAI/pull/32
  - https://www.nngroup.com/articles/progressive-disclosure/
  - https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-faq/
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
tags: ["Engineering", "AI-Native", "UniTutor", "UX", "a11y"]
type: "wiki"
---

# UniTutor PathChrome: 접힘 기본 · 로컬 expanded · CF single-env gate

Eric Option A (Intent Pass): 공부 캔버스 진입 후 Path chrome 기본은 **접힘** — 활성 개념 1줄 + 「경로」토글. 펼치면 PathView·과정 액션. Progressive disclosure(자주 쓰는 현재 개념 1차, 전체 경로 2차).

## UI 계약

- `expanded`는 **로컬 UI state**만 — PathItem/DAG 스키마 필드 아님.
- Detour active도 접힘 유지 + 「우회」배지·우회 개념 제목(자동 펼침 없음).
- a11y: toggle `button` + `aria-expanded` + `aria-controls` + `aria-label`; 접힌 패널은 조건부 렌더로 탭 순서에서 제외.
- App 스모크는 경로 액션/BYOK/알림 전에 토글 클릭이 필요함.

## 배포 / 증거 (merge `73178e8`)

- UniTutor는 Cloudflare single-env (`deploy.yml` on main) — k8s `tenant_cd` / `.factory/cd.yaml` 없음 (`ta.tenant_cd[]` = nl2sql only).
- PR [#32](https://github.com/yoosungung/UniTutorAI/pull/32) → Deploy run 38196130315 success; smoke `api.tutor.askwho.net/health`·`unitutor.askwho.net/` 200.
- QA Playwright(mobile): default collapsed → expand → PathView → detour「우회」while collapsed; bundle `index-CNUNvGqh.js`에 PathChrome a11y 문자열.
- prod gate = main SHA 일치 + Deploy success + public smoke 재확인 (단일 환경이므로 test/prod 분리 없음).
- `aa: N/A` (UI-only local state). Deploy 런북: [[wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md]].
