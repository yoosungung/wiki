---
id: inbox-sql-mcp-hierarchy-schema-store-describe
agent: sql-mcp
ticket_id: ecf04706-af41-4a85-860c-7808727b2fde
updated: 2026-11-14
status: inbox
sources:
  - ticket:ecf04706-af41-4a85-860c-7808727b2fde
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
  - https://github.com/yoosungung/sql-mcp/pull/2
---

# sql-mcp cube.hierarchies 구현

- `$defs.hierarchy`: name + levels(≥2 unique, coarse→fine dim names) + optional description; `cube.hierarchies[]` optional; AP:false; role_playing 미추가.
- libSQL `meta_cube_hierarchies` + store 분해/재조립; links 검증 levels⊆dimension names.
- `describe_table` 응답 optional `hierarchies[]` = drill GROUP BY 순서 힌트(컴파일러 auto-expand 없음).
- 증거: unit `hierarch` + http `api_meta_cube_hierarchies_roundtrip`; PR #2.
