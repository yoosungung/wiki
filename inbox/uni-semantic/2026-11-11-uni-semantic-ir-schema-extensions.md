---
id: inbox-uni-semantic-ir-schema-extensions
agent: uni-semantic
ticket_id: dc3ff9fe-f924-483c-a9c6-96dfdd27fa11
updated: 2026-11-11
status: inbox
sources:
  - ticket:dc3ff9fe-f924-483c-a9c6-96dfdd27fa11
  - https://github.com/yoosungung/uni-semantic
---

# uni-semantic IR §3 확장 최소 shape

- 출발: sql-mcp `document.schema.json` **복사** 후 `$id`만 `https://uni-semantic.local/ir/document.schema.json` (패키지 참조 금지).
- `$defs.dialect`: 방언 태그 문자열(`dax`/`lookml`/`lod`/`mstr`/`sql` …).
- `$defs.unresolved_expression`: required `dialect`+`expression`+`warning`; 멤버 필드명 `unresolved`.
- `$defs.hierarchy`: `name` + `levels`(≥2, 거친→세밀 dimension name); `cube.hierarchies[]`.
- `$defs.role_playing`: `name`+`base_dimension`+`role`; `cube.role_playing[]`.
- snowflake: `viewJoin.snowflake_path` stub만 (Phase 2 본구현 금지).
- 검증: `cd ir && npm test` (Ajv 2020-12).
