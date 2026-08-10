---
id: inbox-nl2sql-ticket391-describe-budget-warehouse-only
agent: nl2sql
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - ticket:391#1368
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #391 AC3: describe char budget + warehouse-only SSE

- local022 empty SQL: multi-round describe with fat valueDomains pushed context to 41886>40960 BadRequest.
- Fix: describe keeps valueDomain on ≤4 columns, members≤8, drops expression, enforces DESCRIBE_JSON_CHARS_MAX=12000.
- local008 `baseball_batting`: MCP error / semantic-only was scored as SSE sql; execute error no longer falls back to input semantic; analyst end emits warehouse_sql only.
