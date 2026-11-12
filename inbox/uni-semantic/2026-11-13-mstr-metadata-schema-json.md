---
id: inbox-uni-semantic-2026-11-13-mstr-metadata-schema-json
agent: uni-semantic
ticket_id: 8c7085b8-d1ab-49b7-8b88-c2b375aafcfa
updated: 2026-11-13
status: inbox
sources:
  - ticket:8c7085b8-d1ab-49b7-8b88-c2b375aafcfa
  - https://github.com/yoosungung/uni-semantic/pull/13
  - https://microstrategy.github.io/rest-api-docs/common-workflows/modeling/manage-table-objects/retrieve-a-tables-definition
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
---

# MSTR Modeling REST Schema JSON → IR (uni-semantic)

- PoC input: 합성 Schema JSON (`tables[]` = `GET /api/model/tables/{id}` subset + `relationships[]`); 실테넌트 HTTP·시크릿 Non-goals (Spotfire IL과 동일).
- Map: `physicalTable.columns` → IR `table`; `tableKey`+ID form `expression.text` → `pk`; parent attr on relationshipTable → `fk`/`viewJoin`.
- `$defs` additive 없음. Crate: `frontend_mstr` · `cargo test -p frontend_mstr`.
- 비범위: live client, freeform SQL table, fact/metric Dialect Transpiler.
