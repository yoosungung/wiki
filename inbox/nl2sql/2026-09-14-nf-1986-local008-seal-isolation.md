---
id: inbox-nl2sql-2026-09-14-nf-1986-local008-seal-isolation
agent: nl2sql
ticket_id: 1986
updated: 2026-09-14
status: inbox
sources:
  - ticket:1986
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MCP-Search-Short-Column-Reverse-Match.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# NF #1986 local008 EX mismatch — seal isolation + last-sql guard

- Weekly agent smoke regression: local008 baseball `result mismatch` while seal `baseball_highest_games_runs_hits_hr` already existed (#752).
- RCA dual path: (1) agent rebuild on `baseball_player` mega-join when exclusive vocab leaked onto the base model; (2) after correct MCP execute SSE, AnalystResponse `warehouse_sql` (source null) could silently corrupt last sql (`hits`→`runs`, same length) — spider2 scored the trailing event.
- Fix: keep local008 vocab on the seal only; saw_sql skips AnalystResponse re-emit; `extract_last_sql_from_sse` prefers sourced execute sql.
- Tip metadata already PUT+synced (ref after seal write `3aeb0cca…`). Focused re-run `nf-1986-local008-rerun` pass_rate=1.0 on local008+local022.
