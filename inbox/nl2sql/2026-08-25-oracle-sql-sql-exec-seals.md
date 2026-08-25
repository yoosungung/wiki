---
id: inbox-nl2sql-2026-08-25-oracle-sql-seals
agent: nl2sql
ticket_id: 1269
updated: 2026-08-25
status: inbox
sources:
  - ticket:1269
  - ticket:1266
---

# oracle_sql sql_exec — MDL name vs warehouse

- Cluster `sql_exec_failed/metadata`: agent invents `states` or uses bare `oracle_sql_inventory` in warehouse FROM (relation missing / syntax near FROM).
- Warehouse tables are `oracle_sql.inventory`, `locations`, `picking_line`, `packaging`, `packaging_relations` — not `states` or schema-prefixed invent names.
- local272 gold EX: `picking_line`+`locations` refSql (not FIFO rebuild on inventory); local270: recursive `packaging_relations` refSql matches gold exec CSV on spider2db PG.
