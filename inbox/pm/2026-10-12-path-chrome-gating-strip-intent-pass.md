---
id: inbox-pm-path-chrome-gating-strip-intent-pass
agent: pm
ticket_id: 793c7592-3071-4ab1-a07b-f96a9ee8703c
updated: 2026-10-12
status: inbox
sources:
  - ticket:793c7592-3071-4ab1-a07b-f96a9ee8703c
  - https://github.com/yoosungung/UniTutorAI/pull/32
  - https://www.nngroup.com/articles/progressive-disclosure/
---

# UniTutor PathChrome gating strip (Intent Pass)

- Eric 승인 Option A: 캔버스 기본은 과정 제목 1줄 + 「경로」토글; 펼치면 PathView·과정 액션.
- 구현은 로컬 `expanded` UI state만 — Path/DAG 스키마 변경 없음. Detour는 접힘 유지 + 「우회」배지.
- Merged: `yoosungung/UniTutorAI#32` → `73178e81677b9c9c81ff72440e2196a06680d848`.
- Progressive disclosure: 자주 쓰는 현재 개념은 1차, 전체 경로·패널은 2차(NN/g 패턴과 정합).
