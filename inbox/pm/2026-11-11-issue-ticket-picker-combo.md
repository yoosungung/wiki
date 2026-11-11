---
id: inbox-pm-issue-ticket-picker-combo
agent: pm
ticket_id: 35557b59-f071-4c75-a598-0d9d29a0d7bc
updated: 2026-11-11
status: inbox
sources:
  - ticket:35557b59-f071-4c75-a598-0d9d29a0d7bc
  - wiki/Engineering/AI-Native-Engineering/Factory-Issue-Details-Parent-Children.md
---

# Issue Details ticket picker (7d / not-Done combo)

- Parent/Blocked-by UUID 수동 입력은 인간 UX 병목; MCP는 id 유지.
- Intake AC: `exclude_done` list + client 7일 `created_at` 콤보, UUID paste 폴백; Children은 생성 유지 + 기존 티켓 연결.
- 계약 변경 없이 FE 우선; miss 시 같은 PR에서 `/api/search` typeahead 최소 추가 가능.
- Parent=`milestone_id` ≠ FS `dependencies` 분리 유지.
