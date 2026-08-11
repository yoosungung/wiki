---
id: inbox-nl2sql-ticket391-sql-quality-fix
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-11-ticket391-test-6572a7b-ac3-fail.md
---

# #391 follow-up: score MCP warehouse only after test-6572a7b

## Problem (SoT 1829)

AC3 on `test-6572a7b` → empty-SQL=0 (task-guard OK) but pass_rate=0. local008 invent `baseball_player_batting_stats`; local022 incomplete SQL (`missing FROM-clause`); overflow ~40998>40960.

## Fix

- Execute SSE: no MDL invent input fallback; fixture SELECT-without-FROM only.
- Analyst SSE: stash `warehouse_sql` only (+ saw_sql warehouse-shaped upgrade).
- Budgets tightened; prompt bans compound invent + FROM-clause retry.

## Verify

pytest 92 passed. Live AC3 remains TA after merge/deploy.
