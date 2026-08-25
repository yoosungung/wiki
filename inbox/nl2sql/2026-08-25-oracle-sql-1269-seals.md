---
id: inbox-nl2sql-2026-08-25-oracle-sql-1269-seals
agent: nl2sql
ticket_id: 1269
updated: 2026-08-25
status: inbox
sources:
  - ticket:1269
  - https://github.com/yoosungung/nl2sql/pull/118
---

# oracle_sql sql_exec — picking_line gold path

- local272 gold exec_result matches `picking_line` JOIN `locations` for order_id=423 (not FIFO recompute from inventory alone).
- Warehouse has no `states` or `oracle_sql_inventory` tables — those are agent inventions when MDL missing.
- local270 recursive packaging CTE: roots = packaging ids not in `packaging_relations.contains_id`.
