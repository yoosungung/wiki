---
id: inbox-nl2sql-ticket795-local167-dec31-seal
agent: nl2sql
ticket_id: 795
updated: 2026-08-14
status: inbox
sources:
  - ticket:795
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Semantic-View-Single-Master.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# local167 sql_exec: first-state Dec-31 seal (city_legislation)

- Scoreboard syntax `near "ORDER"`: live `city_legislation_legislator` mashed term grain + date-dim on `date = term_start` (not BETWEEN). Agent invented window ORDER BY.
- Split single-master legislator/term/date-dim. Seal `city_legislation_female_first_state_dec31` = female + first-term ROW_NUMBER + Dec 31 BETWEEN; gold_b CA/25; CAST bigint.
- Do not copy IPL/modern_data seals or join `cities`. Catalog: `mcp/tests/search_city_legislation_catalog.rs`. MCP `/ready` HEAD can lag; chat lazy-fetches backend ref.
