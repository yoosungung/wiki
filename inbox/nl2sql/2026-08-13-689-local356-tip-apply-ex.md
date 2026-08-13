---
id: inbox-nl2sql-689-local356-tip-apply-ex
agent: nl2sql
ticket_id: 689
updated: 2026-08-13
status: inbox
sources:
  - ticket:689
  - inbox/ta/2026-08-13-689-nl2sql-metadata-tip-resync.md
  - inbox/nl2sql/2026-08-13-f1-overtake-catalog-tip-gap.md
  - spider2-eval/DESIGN.md
---

# #689 tip apply + local356 EX delta

- After TA tip PVC resync (`main`@`6ea134a`, f1×52), Boy Scout overtake vocab PUT on tip `f1_lap`/`f1_pit_stop`/`f1_retirement`/`f1_driver` succeeded: push+MCP sync OK → head `c1e705c…`.
- `spider2-opik run --task agent --instance-ids local356` (`local356-689-overtake`): **empty_sql cleared** (search hits + warehouse SQL emitted) but **pass_rate 0**.
- Agent SQL uses LAG on `lap_times.position` + empty `pit_stops`/`retirements` exclusions; PG counts `pit_stops=0`, `retirements=0` while gold_tables list those tables. `spider2-localdb` zip path missing under `.tmp-spider2` → cannot re-verify full SQLite seed in-session.
- Naive Race-only `lap_positions` LAG intersects only 2/76 gold names → remaining gap is EX semantics/data, not tip catalog miss.
