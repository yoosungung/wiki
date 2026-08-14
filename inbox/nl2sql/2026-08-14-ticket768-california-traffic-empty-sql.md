---
id: inbox-nl2sql-ticket768-california-traffic-empty-sql
agent: nl2sql
ticket_id: 768
updated: 2026-08-14
status: inbox
sources:
  - ticket:768
  - wiki/Agents/Text-to-SQL/Semantic-View-Single-Master.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - https://github.com/yoosungung/nl2sql/pull/95
---

# california_traffic empty_sql (local018 cluster)

- tip `california_traffic_collision_collision` with unjoined inners (`case_ids`/`collisions`/`parties`/`victims`) produces `mdl_translation_error: multiple master inner tables` → empty_sql (same shape as #698/#753).
- Fix: master=`collisions` + left join `case_ids`; party grain split to `california_traffic_collision_party`; refSql seals for local018 PCF 2011−2021 share, local017 unique top-2 year, local015 helmet_worn/no_helmet fatality rate.
- Search regression: `mcp/tests/search_california_traffic_catalog.rs`. Do not put SWITRS/helmet rules in agent prompts.
- Backend metadata HEAD can move while MCP `/ready` HEAD stays on an older SHA; chat still lazy-fetches by ref.
