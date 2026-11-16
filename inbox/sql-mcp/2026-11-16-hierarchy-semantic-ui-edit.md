---
id: inbox-sql-mcp-hierarchy-semantic-ui-edit
agent: sql-mcp
ticket_id: a506b29f-5f3a-4fd5-b254-36b808d0bd89
updated: 2026-11-16
status: inbox
sources:
  - ticket:a506b29f-5f3a-4fd5-b254-36b808d0bd89
  - https://github.com/yoosungung/sql-mcp/pull/3
  - wiki/Engineering/AI-Native-Engineering/Sql-Mcp-Hierarchy-Role-Playing.md
---

# sql-mcp semantic-ui hierarchy 편집

- CubeMappingEditor 하단에 Hierarchies: 순서 있는 dim levels(coarse→fine), Apply 시 `levels ⊆` 활성·expression dimension names · ≥2 unique · name 필수 — 실패 시 alert로 Apply 차단.
- hierarchies 목록이 비면 키 생략(스키마/store additive clear와 동일).
- 순수 검증: `hierarchyLevelsError` / `hierarchyError` in `semantic-ui/src/model.ts`.
- 증거: `cd semantic-ui && npm test` 103 passed · PR #3.
