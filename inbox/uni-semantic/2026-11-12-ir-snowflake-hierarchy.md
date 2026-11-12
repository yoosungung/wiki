---
id: inbox-uni-semantic-ir-snowflake-hierarchy
agent: uni-semantic
ticket_id: 68f4207a-e514-48cb-9243-f5d77c83e652
updated: 2026-11-12
status: inbox
sources:
  - ticket:68f4207a-e514-48cb-9243-f5d77c83e652
  - https://github.com/yoosungung/uni-semantic/pull/11
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
---

# uni-semantic: IR snowflake_path + Hierarchy Phase 2

- `$defs.snowflake_path` extracted; `viewJoin.snowflake_path` $ref; omit=direct join; empty array invalid (`minItems` 1).
- Hierarchy additive optional `description`; levels ≥2 unique unchanged.
- Fixtures: `view-orders_region_snowflake.json`, `cube-sales-hierarchy.json` (3-level), invalid empty-path / dup-levels.
- Verify: `cd ir && npm test`.
