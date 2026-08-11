---
id: inbox-nl2sql-ticket391-stash-budget-fix
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-11-ticket391-test-3648949-ac3-fail.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #391 follow-up: stash-first SSE + tool budgets after test-3648949

## Problem (SoT 1720)

AC3 on `test-3648949` → pass_rate 0.0. local022 empty SQL; local008 invented `baseball_players`; analyst path BadRequest `62534>40960`.

## Fix (branch feature/391-ac3-3648949-stash-budget)

- Analyst SSE: MCP execute stash first; structured `warehouse_sql` only if schema.table / quoted (blocks invent).
- Tool budgets: describe≤6k, search≤1k, ondemand≤1.5k, multi-turn≤11k; members max 2; describe_columns request max 4.

## Verify

Focused backend pytest 90 passed. Live AC3 remains TA after merge/deploy.
