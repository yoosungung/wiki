---
id: inbox-nl2sql-ticket391-warehouse-emit-fix
agent: nl2sql
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - wiki/Engineering/AI-Native-Engineering/On-Demand-Schema-Describe-Tools.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - inbox/ta/2026-08-11-ticket391-prod-f9622ab-ac3-fail.md
---

# #391 follow-up: force warehouse_sql after tip f9622ab

## Problem (SoT 1610)

AC3 on `prod-f9622ab` → empty-SQL=2, pass_rate=0. Analyst ended with `warehouse_sql: null`, invented non-MDL names (`players_stats`/`table_1`), and burned turns on empty `task` `{}`.

## Fix (branch feature/391-ac3-f9622ab-warehouse-emit)

- Analyst + orchestrator prompts: require execute→copy warehouse; forbid invented tables; cap on-demand describe; ban empty task kwargs.
- `AnalystResponse` after-validator: non-empty `semantic_sql` requires `warehouse_sql` unless caveats contain `empty catalog` (structured-output retry).
- DESIGN §2.4 #391 note updated.

## Verify

`pytest` analyst_response / value_domain / chat / sse helpers / execute stash — pass. Live AC3 remains TA after merge/deploy.
