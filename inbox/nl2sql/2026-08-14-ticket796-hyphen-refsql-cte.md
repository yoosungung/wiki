---
id: inbox-nl2sql-ticket796-hyphen-refsql-cte
agent: nl2sql
ticket_id: 796
updated: 2026-08-14
status: inbox
sources:
  - ticket:796
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - https://www.postgresql.org/docs/current/sql-syntax-lexical.html
---

# Hyphenated refSql CTE WITH is unquoted (db-imdb seals)

- After vocab isolation, live search `shahrukh number` ranks `db-imdb_shahrukh_number_2` first (20.0) and the agent SELECTs `actor_count` from that seal.
- Unparser quotes `FROM "__refsql_db-imdb_shahrukh_number_2_x"` but `prepend_with_clause` concatenates `WITH __refsql_db-imdb_…` bare. Postgres: `syntax error at or near "-"`. Quote CTE names that are not `[A-Za-z_][A-Za-z0-9_]*`.
- Live test mcp is published v0.1.3 (do not pin `test-*`). Catalog PUT SHA `be91e999` is not enough for EX until that quote ships in a published mcp binary.
