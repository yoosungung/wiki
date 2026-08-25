---
id: inbox-pm-2026-08-25-ticket-1269-oracle-sql-intake
agent: pm
ticket_id: 1269
updated: 2026-08-25
status: inbox
sources:
  - ticket:1269
  - ticket:1266
---

# #1269 oracle_sql metadata intake (sql_exec_failed)

- **Wave:** #1266 improve seq 2/5 · cluster `sql_exec_failed/metadata` · schema `oracle_sql` · n=3 (rep `local272`, siblings `local279`/`local270`).
- **1차 레버:** metadata — `states` / `oracle_sql_inventory` relation·FROM vs warehouse; invent relation/FROM 금지 (wiki: Spider2-Quality-Gate-nl2sql).
- **독립 스키마:** blocked-by 없음; #1267 spider2-eval PR 병렬 OK.
- **tip gate:** tenant sync `origin/main` ≥ `48e1795` (#1261 bundle); ephemeral `/tmp/tenant-repos/nl2sql` @ `dc8a7bc` satisfies.
- **AC 요약:** (1) oracle_sql `*.model.json` relation/refSql warehouse 정합 (2) live SSE local272+sibling sql_exec 해소 (3) metadata push+sync ack (4) PR → Review @pm (5) prompt hardcode 금지.
- **RCA 힌트:** unknown relation / missing FROM → MDL name vs warehouse; syntax near FROM이 refSql 쪽이면 seal 수정; mcp unparse는 tip 증거 후에만.
