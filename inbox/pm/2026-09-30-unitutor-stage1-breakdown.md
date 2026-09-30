---
id: inbox-pm-unitutor-stage1-breakdown
agent: pm
ticket_id: 82c5e37b-e839-4e9d-ab1c-af1496d3558a
updated: 2026-09-30
status: inbox
sources:
  - ticket:82c5e37b-e839-4e9d-ab1c-af1496d3558a
  - repo:yoosungung/UniTutorAI ROADMAP.md###1단계
---

# UniTutorAI 1단계 마일스톤 breakdown

- UniTutorAI 첫 마일스톤은 「강의 보면서 질문받기」: 정적 VTT/슬라이드 배치 + 적응형 2분할 + YouTube iframe + TutorTurn 1질문/CitationSelected.
- ROADMAP §2 미결정(첫 과목 CS50 vs 선형대수)이 VTT 가공의 선행 게이트. 캔버스는 placeholder CourseRef로 병렬 가능.
- 테넌트 ROADMAP이 `###`+plain bullet이라 factory checklist sync는 no-op — 일상 sync용으로는 `##`+`- [ ]` 정합이 유리.
- 계약 식별자(`CourseRef`/`SourceSpan`/`TutorTurn`)는 유지; 플레이어 오버레이·풀이 전문 튜터는 Non-goal.
