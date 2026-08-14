---
id: inbox-pm-ticket784-local073-sql-exec-merged
agent: pm
ticket_id: 784
updated: 2026-08-14
status: inbox
sources:
  - ticket:784
  - https://github.com/yoosungung/nl2sql/pull/100
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - inbox/nl2sql/2026-08-14-ticket784-local073-sql-exec-seal.md
---

# local073 sql_exec seal merged (NF Done)

- Scoreboard `near ".."` was SQLite `INSTR`/`SUBSTR` CSV splits on PG. Seal `modern_data_pizza_order_final_ingredients` uses `string_to_array`/`unnest`/`string_agg` + `COLLATE "C"` (refSql vs gold_a 14/14). Do not copy #783 income prices.
- PR #100 merged `merge_sha=8048c28e50b484c1d30e2463faa7446cea555d75`. Agent EX local073 sql_exec cleared is NF Done evidence; residual result_mismatch (CASE concat on `modern_data_pizza`, 15 vs gold 14) is out of AC. `.factory/quality.yaml` has no tenant_cd — not Deploying Test.
