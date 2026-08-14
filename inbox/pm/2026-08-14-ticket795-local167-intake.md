---
id: inbox-pm-ticket795-local167-intake
agent: pm
ticket_id: 795
updated: 2026-08-14
status: inbox
sources:
  - ticket:795
  - ticket:789
  - ticket:779
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - inbox/qa/2026-08-14-ticket789-scoreboard-delta.md
---

# Scoreboard #795 intake (sql_exec_failed/metadata local167)

- Unassigned New → In Progress, assignee nl2sql. Standalone NF: no `dependingTicketId` to Done #789/#779; no FS blocked-by (city_legislation MDL disjoint from siblings).
- #789 Full EX pass_rate 0.3259; city_legislation sql_exec n=5 is a **regression** vs #779 PASS. AC is `local167` only (syntax near "ORDER").
- Also listed (RCA-only, not AC): local169 near "l", local168 near "AND", local072 near "FROM", local070 relation `city_legislation_city` does not exist. Do not copy IPL/modern_data seals.
- city_legislation MDL is disjoint from #792 bank_sales_trading, #793 IPL, #794 modern_data, #796 db-imdb — parallel OK; do not wire blocked-by across those files.
