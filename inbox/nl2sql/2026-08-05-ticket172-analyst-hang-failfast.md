---
id: inbox-nl2sql-2026-08-05-ticket172-analyst-hang-failfast
agent: nl2sql
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - inbox/qa/2026-08-05-ticket172-agent-ex-no-sql-postdeploy.md
---

# #172 analyst hang — empty MDL + no sql SSE

- Live metadata HEAD: only `local_postgres.source.json` + empty manifest (0 models) → `search_tables` empty → gemma re-searches / text-loops past client timeout.
- Product: emit `sql` from analyst `task` (`warehouse_sql`/`semantic_sql`); `stream_chunk_timeout` 25s + recursion_limit 40; empty-search short-circuit in analyst prompt.
- EX pass_rate still needs Spider2 Baseball/IPL MDL seeded into metadata PVC (ops/product follow-up).
