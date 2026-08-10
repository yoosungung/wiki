---
id: inbox-nl2sql-ticket391-execute-sse-stash-box
agent: nl2sql
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - ticket:391#1419
  - https://github.com/yoosungung/nl2sql/pull/48
---

# #391 AC3: shared execute SSE stash box

- After warehouse-only SSE (#48), smoke empty-SQL became 2: runs finished, no BadRequest, but no usable warehouse_sql on SSE.
- Cause: deepagents/LangGraph `copy_context()` — child `ContextVar.set(payload)` not visible to parent pop.
- Fix: request-scoped shared dict in ContextVar; analyst end recovers stashed warehouse when parent missed execute tool_end.
