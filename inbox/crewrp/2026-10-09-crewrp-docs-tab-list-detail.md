---
id: inbox-crewrp-2026-10-09-docs-tab-list-detail
agent: crewrp
ticket_id: 512000ad-8c3f-4f06-8604-9511b81ca218
updated: 2026-10-09
status: inbox
sources:
  - ticket:512000ad-8c3f-4f06-8604-9511b81ca218
  - repo:yoosungung/crewrp
---

# CrewRP 자료실 목록→상세 UX

- DocsTab: 가로 칩+본문 split 제거 → 파일·폴더 목록 + 시트/다이얼로그 상세.
- `filterDocs`·`parentDocsPath`는 ShellPresentation(core). Contents API는 path lazy 드릴다운.
- 검색은 이름·경로 부분 일치(대소문자 무시); 본문 grep Non-goal.
