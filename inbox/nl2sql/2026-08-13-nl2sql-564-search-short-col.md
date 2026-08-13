---
id: inbox-nl2sql-564-search-short-col
agent: nl2sql
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - ticket:391
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# nl2sql #564: schema-prefix search ranked fielding over batting

- Live tip `test-d28fadc` + luna: agent smoke empty_sql=0 but pass_rate=0 (`result mismatch`). local008 search `baseball`/`baseball stats` returned `baseball_fielding*` (mcp log score 11–13).
- Root cause: MCP `score_column` reverse match `token.contains(col)` let 1-char cols (`g`,`a`,`e`) ride inside schema token `baseball`, tying/boosting fielding; analyst prompt also told the model to search the schema name.
- Fix direction: ignore reverse col match unless col len≥4; strip redundant schema tokens when schema filter set; backend enrich schema-only/`{schema} stats` queries from question keywords; prompt uses metric keywords not schema-only.
