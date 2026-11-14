---
id: inbox-uni-semantic-sql-mcp-role-playing-strip
agent: uni-semantic
ticket_id: 8066ed99-6288-452e-bb2d-7b7bf6412a51
updated: 2026-11-14
status: inbox
sources:
  - ticket:8066ed99-6288-452e-bb2d-7b7bf6412a51
  - ticket:8709c016-1ea3-4e7b-9112-370c53dce3d6
  - inbox/sql-mcp/2026-11-14-hierarchy-role-playing-decision.md
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
  - repo:uni-semantic/ARCHITECTURE.md
---

# uni-semantic: sql-mcp emit role_playing strip 계약

- ARCHITECTURE §5.1: Phase 4 MVP에서 IR→sql-mcp emit 시 `cube.role_playing[]` **strip**; hub IR 필드는 유지.
- 부모 sql-mcp `decision: partial` — role_playing reject+strip; sql-mcp는 dimension+view join alias로만 role-play.
- 후속(선택): emit 전 dimension+join alias 전개 어댑터 — MCP emit 본구현 티켓 밖.
- PR: https://github.com/yoosungung/uni-semantic/pull/18
