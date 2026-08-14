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
---

# california_traffic empty_sql (local018 cluster)

- tip `california_traffic_collision_collision` with unjoined `case_ids`/`collisions`/`parties`/`victims` produces `mdl_translation_error: multiple master inner tables` → empty_sql (#698/#753 shape).
- Fix: master=`collisions` + left join `case_ids`; split parties to `california_traffic_collision_party`; refSql seals for local018/017/015.
- Search regression: `mcp/tests/search_california_traffic_catalog.rs`. Do not put SWITRS/helmet rules in agent prompts.
- local017 gold year 2021 vs live PG unique top-2 year 2001 is result_mismatch residual, not empty_sql.
