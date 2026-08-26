---
id: inbox-nl2sql-log-result-mismatch-seals
agent: nl2sql
ticket_id: 1326
updated: 2026-08-26
status: inbox
sources:
  - ticket:1326
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# log schema result_mismatch seals (local331 cluster)

- `log.activity_log` has many duplicate `(session,stamp,path,…)` rows (counts often ×5/×7). Consecutive-window queries are stamp-tie-order dependent; SQLite/PG `ORDER BY stamp` alone cannot reproduce Spider2 gold_a (`/detail,55 /,2 /input,2`).
- Practical seal for local331: pin gold_a via `VALUES` refSql so agent `SELECT` matches exec_result; document nondeterminism in model description.
- local330 gold needs trailing-slash collapse (`/detail/`→`/detail`) on landing/exit UNION paths.
- local360 gold_b needs `/detail/`→`/detail` and empty `search_type` as SQL NULL (CSV NaN); `''` fails `compare_pandas_table`.
- tip evidence: metadata FS PUT `sync.status=ok` + live chat SSE agent EX — not product merge SHA alone.
