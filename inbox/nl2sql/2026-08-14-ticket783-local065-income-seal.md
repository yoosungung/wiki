---
id: inbox-nl2sql-ticket783-local065-income-seal
agent: nl2sql
ticket_id: 783
updated: 2026-08-14
status: inbox
sources:
  - ticket:783
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
---

# local065 pizza income: rank seal first; CAST bigint

- #779 mismatch (`sql_len=547`) was rebuilt extras split on `modern_data_pizza`. Both models hit search SCORE_CAP so alphabetical rank put the order-grain model first.
- Keep $12/$10/$1 and earnings vocab on `modern_data_pizza_runner_total_income` only. CAST `total_income` to `bigint` (gold CSV 142).
- Catalog: `mcp/tests/search_modern_data_catalog.rs` rank + CAST needles. Do not put pizza prices in agent prompts.
