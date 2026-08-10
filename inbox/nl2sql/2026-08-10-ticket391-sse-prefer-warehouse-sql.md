---
id: inbox-nl2sql-ticket391-sse-prefer-warehouse-sql
agent: nl2sql
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - ticket:391#1294
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #391 AC3: SSE prefer warehouse_sql

- After schema-hint PR #43, AC3 empty-SQL=0 but pass_rate=0: last SSE `sql` was semantic/garbage (`\x08`, `players_stats`) not MCP warehouse SQL.
- Fix: execute SSE prefers stash `warehouse_sql`; analyst end with prior execute only upgrades via warehouse; skip C0-control SQL in extract (backend + eval).
- Residual risk: if execute never succeeds, semantic-only wrong-relation SQL can still score 0 — needs successful execute or harder schema routing.
