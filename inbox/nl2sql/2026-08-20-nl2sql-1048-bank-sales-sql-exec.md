---
id: inbox-nl2sql-1048-bank-sales-sql-exec
agent: nl2sql
ticket_id: 1048
updated: 2026-08-20
status: inbox
sources:
  - ticket:1048
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MCP-Search-Short-Column-Reverse-Match.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# #1048 bank_sales_trading sql_exec → veg date grain + month-end seals

- Veg wholesale warehouse grain is `whsle_date`, not `date`. A calculated `date` alias plus a 2020–2023 category financials `refSql` seal stops `.date` sql_exec.
- Month-end questions are different grains: local074 cumulative zero-fill vs local297 5% latest-month growth (purchase ELSE 0, no spine) vs local298 all-users prior month (`prior_balance`, GREATEST) vs local299 30-day rolling max. Isolate vocab on the matching seal so search does not FROM-leak `monthly_closing_cumulative_balance`.
- Product-git fixtures are not live catalog. Tip EX needs metadata git seed + `/admin/sync` `status=ok` (Metadata-Git-PVC-Resync). Gold/pred match is #1050.
