---
id: inbox-nl2sql-ticket794-local073-convert-to
agent: nl2sql
ticket_id: 794
updated: 2026-08-14
status: inbox
sources:
  - ticket:794
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# local073: seal SELECT works after dropping COLLATE from refSql

- Search already ranked `modern_data_pizza_order_final_ingredients` first; agent still emitted pizza SQL because MCP rewrite of `COLLATE "C"` failed (`ParserError COLLATE`) and execute_select fell back.
- Gold C-order (`BBQ Sauce` before `Bacon`) is preserved with `convert_to(topping_name, 'SQL_ASCII')` instead of COLLATE. Drop pizza extras/recipes `row_id` leaks so describe cannot fake the grain.
- Agent EX experiment `794-local073-convert-to-ascii` pass_rate 1.0. Tip metadata SHA after PUT `d6be092b` (MCP sync ok). Product git SHA ≠ metadata git SHA.
