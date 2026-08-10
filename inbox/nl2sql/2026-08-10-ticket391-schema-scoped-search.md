---
id: inbox-nl2sql-ticket391-schema-scoped-search
agent: nl2sql
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - ticket:391#1294
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #391 AC3: schema-scoped MCP search + warehouse SSE

- Soft `[Spider2 schema: …]` prompt alone still let keyword search return baseball models for IPL questions → hallucinated `players_stats`.
- Hard pin: optional `search_tables.schema` filters `tableReference.schema`; backend ContextVar forwards the chat hint.
- Separately, last SSE `sql` must be MCP `warehouse_sql` (not semantic / C0-garbage) or Opik scores non-executable SQL under `search_path`.
