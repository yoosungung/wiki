---
id: inbox-nl2sql-ticket789-local073-topping-select
agent: nl2sql
ticket_id: 789
updated: 2026-08-14
status: inbox
sources:
  - ticket:789
  - ticket:784
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# local073 mismatch: topping catalog SELECT, not final-ingredients seal

- After #784 `modern_data_pizza_order_final_ingredients` seal (PR #100), Full EX still fails local073 as `result_mismatch` (sql_len=315).
- Emitted SQL selected `topping_id`/`topping_name` from `modern_data_pizza_topping`, not `SELECT row_id, order_id, customer_id, pizza_name, final_ingredients` from the seal.
- Search-rank fixture at agent k=3 is not enough if describe still lets the topping catalog win the SELECT. Residual belongs on a standalone improve ticket, not reopen of the sql_exec seal.
