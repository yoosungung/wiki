---
id: inbox-nl2sql-ticket391-decimal-stash-emit-fix
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-11-ticket391-test-6b63138-ac3-fail.md
  - wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md
---

# #391 tip test-6b63138 — decimal + prose stash emit

- SoT: overflow/timeout/infinity 0 after PR #58; empty-SQL=2 from MCP `dialect_unparse_failed` (bare `decimal` on `baseball_all_star.gp`) and channel-thought/prose stop without SSE sql.
- Fix: `arrow_type("decimal"|"numeric")` → Decimal128(38,10); schema vocab; `_to_sse` emits stash warehouse_sql before `done` on normal end.
- Verify: backend pytest 33 passed; mcp compile needs CI (`cc` missing in Pod).
