---
id: inbox-nl2sql-689-local356-post-wipe-ex
agent: nl2sql
ticket_id: 689
updated: 2026-08-13
status: inbox
sources:
  - ticket:689
  - inbox/nl2sql/2026-08-13-689-f1-pit-reload-lap-type-mdl.md
---

# #689 local356 EX after Eric tip wipe+reclone

- Tip verify: backend+mcp ready, metadata head `2e5bd9b`, `f1_lap` has overtake+pairwise vocab; PG pit_stops=10990 / retirements=11568.
- Experiment `local356-689-post-wipe-reclone`: pass_rate 0 (not empty_sql; warehouse SQL path). Catalog+data OK; EX residual remains agent-SQL scope per #3336.
