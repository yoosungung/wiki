---
id: inbox-nl2sql-ticket794-local073-seal-select
agent: nl2sql
ticket_id: 794
updated: 2026-08-14
status: inbox
sources:
  - ticket:794
  - ticket:784
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# local073 mismatch: topping SELECT, not final-ingredients seal

- After #784 seal, agent EX still `result_mismatch`. Vocab isolation (keep “final ingredients” off pizza/topping descriptions) + drop `pizza.row_id` (`pizza_get_exclusions` 15-row fanout) did not make the agent `SELECT` the seal.
- Latest EX `794-local073-no-pizza-rowid`: sql_len=318 `SELECT topping_id, topping_name FROM modern_data_pizza_topping` (matches Full EX ~315). Prior EX after vocab-only still rebuilt on `modern_data_pizza`.
- Catalog ranks seal first at agent k=3 for 1–2 keyword queries. Residual: describe/SELECT still prefers topping catalog or pizza grain. Do not copy #783 income prices.
