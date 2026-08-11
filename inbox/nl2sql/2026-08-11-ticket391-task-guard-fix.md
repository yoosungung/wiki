---
id: inbox-nl2sql-ticket391-task-guard-fix
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - inbox/ta/2026-08-11-ticket391-test-117c074-ac3-fail.md
---

# #391 follow-up: EnsureAnalystTaskMiddleware after test-117c074

## Problem (SoT 1792)

AC3 on `test-117c074` → empty-SQL=2, pass_rate=0. local008 `task({})` Field required then empty stop; local022 empty AIMessage stop (no analyst). Overflow gone vs SoT 1720.

## Fix

`EnsureAnalystTaskMiddleware` fills empty task args from last HumanMessage; injects `task(analyst)` on silent stop when schema hint present.

## Verify

pytest test_task_guard + related — pass. Live AC3 remains TA after merge/deploy.
