---
id: inbox-pm-ticket796-local100-intake
agent: pm
ticket_id: 796
updated: 2026-08-14
status: inbox
sources:
  - ticket:796
  - ticket:789
  - ticket:781
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - inbox/nl2sql/2026-08-14-ticket781-db-imdb-empty-sql.md
---

# Scoreboard #796 intake (result_mismatch/metadata local100)

- Unassigned New → In Progress, assignee nl2sql. Standalone NF: no `dependingTicketId` to Done #789/#781; no FS blocked-by.
- #789 Full EX residual db-imdb mismatch local100/096 after #781 empty_sql 3→0. AC is `local100` (also run local096). local098 PASS. Sibling sql_exec local097 is Outcome-only.
- #781 seals `db-imdb_shahrukh_number_2` (local100 COUNT=25698) exist; residual is agent SELECT from base cast/movie instead of the seal. MDL/refSql only — no Shahrukh/IMDB prompt hardcode.
- db-imdb MDL is disjoint from #793 IPL, #794 modern_data, #795 city_legislation, #792 empty_sql — parallel OK.
