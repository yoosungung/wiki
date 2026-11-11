---
id: inbox-sw-factory-issue-ticket-picker-combo
agent: sw-factory
ticket_id: 35557b59-f071-4c75-a598-0d9d29a0d7bc
updated: 2026-11-11
status: inbox
sources:
  - ticket:35557b59-f071-4c75-a598-0d9d29a0d7bc
  - wiki/Engineering/AI-Native-Engineering/Factory-Issue-Details-Parent-Children.md
---

# Issue Details TicketPicker (7d / exclude_done)

- `frontend/.../TicketPicker.tsx`: exclude_done list → client 7d filter + UUID paste; miss 시 같은 project `/api/search` typeahead.
- Parent/Blocked by/Children(link) 인라인 사용; Children 기존 연결은 getTicket.version → PATCH milestone_id OCC.
- MCP/agent id 계약 변경 없음 — SPA UX만.
