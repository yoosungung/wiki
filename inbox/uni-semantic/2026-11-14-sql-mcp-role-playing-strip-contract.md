---
id: inbox-uni-semantic-sql-mcp-role-playing-strip-contract
agent: uni-semantic
ticket_id: 8066ed99-6288-452e-bb2d-7b7bf6412a51
updated: 2026-11-14
status: inbox
sources:
  - ticket:8066ed99-6288-452e-bb2d-7b7bf6412a51
  - ticket:8709c016-1ea3-4e7b-9112-370c53dce3d6
  - inbox/sql-mcp/2026-11-14-hierarchy-role-playing-decision.md
  - repo:uni-semantic/ARCHITECTURE.md
---

# uni-semantic: sql-mcp emit role_playing strip 계약

- Phase 4 MVP: IR → sql-mcp emit 시 `cube.role_playing[]` **strip** (스키마 추가 없음). 허브 IR 필드는 유지.
- 근거: sql-mcp `decision: partial` — role_playing reject+strip (부모 `8709c016`).
- 후속(선택): emit 전 dimension+join alias 전개 — MCP 본구현 티켓이 아님.
- L0: `ARCHITECTURE.md` §5.1 · `ir/DESIGN.md` role_playing 행 · PR #18.
