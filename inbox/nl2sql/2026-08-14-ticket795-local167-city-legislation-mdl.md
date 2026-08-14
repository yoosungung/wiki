---
id: inbox-nl2sql-ticket795-local167-city-legislation-mdl
agent: nl2sql
ticket_id: 795
updated: 2026-08-14
status: inbox
sources:
  - ticket:795
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Semantic-View-Single-Master.md
  - spider2-eval/DESIGN.md
---

# city_legislation local167 sql_exec (metadata seal)

- Product git had no `city_legislation` `*.model.json`. Schema-pinned search misses legislators/date-dim → agent invents window `ORDER BY` → syntax `near "ORDER"` (#789 regression vs #779).
- Gold tables: `legislators`, `legislators_terms`, `legislation_date_dim`. Gold_b = first-represented state of female legislators whose terms BETWEEN-span a date-dim December 31 (`CA`, 25). Gold_a (`CA`, 42) is calendar Dec-31 without the 1917–1999 dim filter — do not seal that path.
- Seal `city_legislation_female_first_state_dec31`: `ROW_NUMBER` first term + dim `month_name='December' AND day_of_month=31`; CAST count `bigint`. Single-master physicals only; do not mash date-dim onto terms (`date = term_start` is wrong). Do not copy IPL/modern_data seals or join `cities`.
- RCA-only (not AC): local070 `city_legislation_city` warehouse leak is #770-shaped; local168/169/072 other syntax.
