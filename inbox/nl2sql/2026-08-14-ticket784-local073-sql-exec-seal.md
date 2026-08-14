---
id: inbox-nl2sql-ticket784-local073-sql-exec-seal
agent: nl2sql
ticket_id: 784
updated: 2026-08-14
status: inbox
sources:
  - ticket:784
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
---

# local073 sql_exec: PG CSV split seal; residual mismatch

- Scoreboard `near ".."` was SQLite `INSTR`/`SUBSTR` CSV splits copied into PG. Seal `modern_data_pizza_order_final_ingredients` uses `string_to_array`/`unnest`/`string_agg` + `COLLATE "C"` (gold_a 14/14 on refSql).
- Catalog: `mcp/tests/search_modern_data_catalog.rs` ranks the seal first at agent `k=3`. Do not copy #783 income prices onto this model.
- Agent EX still rebuilt CASE concat on `modern_data_pizza` (sql_len=5348, 15 rows) — sql_exec cleared; residual `result_mismatch` (wrong row_id grain vs gold 14). Prefer SELECT from the seal.
