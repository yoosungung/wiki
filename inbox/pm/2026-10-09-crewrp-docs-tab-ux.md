---
id: inbox-pm-2026-10-09-crewrp-docs-tab-ux
agent: pm
ticket_id: 512000ad-8c3f-4f06-8604-9511b81ca218
updated: 2026-10-09
status: inbox
sources:
  - ticket:512000ad-8c3f-4f06-8604-9511b81ca218
  - ticket:4ff87fa4-be74-4068-b230-e075e088c108
  - repo:yoosungung/CrewRP
  - wiki/Engineering/Development-Environment/CrewRP-Tasks-Tab-Compact-Kanban.md
---

# CrewRP 자료실 탭 UX intake

- 현재 DocsTab: 상단 가로 파일명 칩 + 동일 화면 본문(split). `isDir` 숨김.
- 목표: 공지/할 일과 같이 목록→상세; `/docs` 폴더 드릴다운(`listDocs(path:)` 기존); 이름·경로 필터 검색.
- Non-goal: 본문 full-text, Contents 계약 변경, Phase 4.
- Contents API는 path 단위 → 전수 재귀보다 lazy 드릴다운 권장(rate limit).
