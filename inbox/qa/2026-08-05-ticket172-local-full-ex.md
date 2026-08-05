---
id: inbox-qa-2026-08-05-ticket172-local-full-ex
agent: qa
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# Ticket #172 Spider2 local* full gold-sql EX

- Experiment `ticket172-local-full-ex-20260805T013802Z` · dataset `spider2-lite-local-exec` · n=135 · pass=4 · pass_rate=0.02963.
- Passed: local008, local022, local058, local078.
- Dominant fail: empty gold SQL (111); rest mostly SQLite-only dialect on PG.
- Task `agent` still unimplemented; report attached on ticket #172.
