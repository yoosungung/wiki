---
id: inbox-pm-ticket794-local073-intake
agent: pm
ticket_id: 794
updated: 2026-08-14
status: inbox
sources:
  - ticket:794
  - ticket:789
  - ticket:784
  - ticket:783
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - inbox/nl2sql/2026-08-14-ticket784-local073-sql-exec-seal.md
---

# Scoreboard #794 intake (result_mismatch/metadata local073)

- Unassigned New → In Progress, assignee nl2sql. Standalone NF: no `dependingTicketId` to Done #789/#779/#784; no FS blocked-by (#784 sql_exec Done, #783 local065 PASS).
- #789 Full EX pass_rate 0.3259; residual modern_data mismatch local073/066/049/040. AC is `local073` only.
- #784 seal `modern_data_pizza_order_final_ingredients` cleared sql_exec; residual was CASE concat on `modern_data_pizza` (15 vs gold 14). Prefer SELECT from that seal; do not copy #783 income prices.
- modern_data MDL is disjoint from #793 IPL, #796 db-imdb, #795 city_legislation, #792 empty_sql — parallel OK; do not wire blocked-by across those files.
