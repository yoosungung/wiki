---
id: inbox-nl2sql-ticket781-db-imdb-empty-sql
agent: nl2sql
ticket_id: 781
updated: 2026-08-14
status: inbox
sources:
  - ticket:781
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
---

# db-imdb empty_sql (local100 cluster)

- Tip `db-imdb_*.model.json` already existed; empty_sql was English vocab miss (Korean-only descriptions) → search_tables 0, not a missing-file gap.
- Seals: `db-imdb_shahrukh_number_2` (local100 COUNT=25698), `db-imdb_actor_no_long_break` (local098 gold_c 28698), `db-imdb_exclusively_female_year` (local096). TRIM PID/Name; quote `"db-imdb"`.
- Agent EX can emit SQL from base cast/movie models and still result_mismatch if it does not SELECT the seal. Do not put Shahrukh/IMDB rules in prompts.
