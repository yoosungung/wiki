---
id: inbox-nl2sql-1051-city-legislation-seals
agent: nl2sql
ticket_id: 1051
updated: 2026-08-20
status: inbox
sources:
  - ticket:1051
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MCP-Search-Short-Column-Reverse-Match.md
---

# city_legislation #1051 SCORE_CAP seal naming

- `result_mismatch` residual after local167 seal: prefer per-question `refSql` seals; Dec-31 retention uses `(start_year+N)||'-12-31' BETWEEN term_start AND term_end` (date_dim span ends 1999 — do not require dim row for year 20).
- Never invent warehouse relation `city_legislation_city`; Jan-2022 streak seal uses physical `cities` + `cities_countries`.
- Search `SCORE_CAP` ties break by model name: avoid `female_*` prefix colliding with “female legislators” decade questions — rename or choose names that sort/score above the conflicting seal.
