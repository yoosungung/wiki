---
id: inbox-uni-tutor-path-chrome-gating-strip
agent: uni-tutor
ticket_id: 793c7592-3071-4ab1-a07b-f96a9ee8703c
updated: 2026-10-12
status: inbox
sources:
  - ticket:793c7592-3071-4ab1-a07b-f96a9ee8703c
  - https://github.com/yoosungung/UniTutorAI/pull/32
  - https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-faq/
---

# UniTutor PathChrome gating strip

- 공부 캔버스 진입 후 Path chrome 기본은 **접힘**: 활성 개념 1줄 + 「경로」토글. 펼치면 PathView·과정 액션.
- `expanded`는 **로컬 UI state**만 — PathItem/스키마 필드 아님.
- Detour active도 접힘 유지 + 「우회」배지·우회 개념 제목(자동 펼침 없음).
- a11y: toggle `button` + `aria-expanded` + `aria-controls` + `aria-label`; 접힌 패널은 조건부 렌더로 탭 순서에서 제외.
- App 스모크는 경로 액션/BYOK/알림 전에 토글 클릭이 필요함.
