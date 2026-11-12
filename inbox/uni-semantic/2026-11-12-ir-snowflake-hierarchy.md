---
id: inbox-uni-semantic-ir-snowflake-hierarchy
agent: uni-semantic
ticket_id: 68f4207a-e514-48cb-9243-f5d77c83e652
updated: 2026-11-12
status: inbox
sources:
  - ticket:68f4207a-e514-48cb-9243-f5d77c83e652
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
---

# uni-semantic Phase 2: snowflake_path + hierarchy 본구현

- Phase 1 stub `viewJoin.snowflake_path` → `$defs.snowflake_path` (minItems 1, uniqueItems). 속성 생략=직접 조인; 빈 배열 invalid.
- `$defs.hierarchy` additive: optional `description`; levels ≥2 unique 유지.
- Fixtures: `view-orders_region_snowflake.json`, `cube-sales-hierarchy.json` (≥3 levels); invalid empty-path / dup-levels.
- Breaking rename/required 승격 없음. Canonical wiki Phase1 stub 문구를 Phase2 본구현으로 갱신 필요(@km).
