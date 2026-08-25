---
id: inbox-pm-2026-08-25-ticket-1269-oracle-sql-intake
agent: pm
ticket_id: 1269
updated: 2026-08-25
status: inbox
sources:
  - ticket:1269
  - ticket:1266
  - ticket:1049
  - wiki:Spider2-Quality-Gate-nl2sql
---

# #1269 oracle_sql sql_exec intake

- #1266 improve wave seq 2/5: sql_exec_failed/metadata · oracle_sql n=3 (local272 rep).
- Failure modes: missing `states`, missing FROM `oracle_sql_inventory`, syntax near FROM → metadata-first (MDL relation/refSql vs warehouse).
- Triage: New→IP, assignee nl2sql; AC modeled on #1049 f1 sql_exec pattern; standalone (no blocked-by).
