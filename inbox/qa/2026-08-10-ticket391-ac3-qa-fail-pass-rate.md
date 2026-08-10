---
id: inbox-qa-2026-08-10-ticket391-ac3-qa-fail-pass-rate
agent: qa
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - https://github.com/yoosungung/nl2sql/pull/41
---

# #391 QA AC3: empty SQL=0 but pass_rate=0

- Live image `test-f4218d3` (merge `f4218d36…`) · health/ready 200 · synced sha `f4218d3`.
- QA re-run: `spider2-opik run --task agent --instance-ids local008,local022` experiment `ticket391-qa-agent-smoke-20260810-023455` id `019fe985-ee63-77f1-ba0c-7c679d2ada33`.
- empty-SQL count **0** (unwrap/SSE extract path OK on both instances).
- pass_rate **0.0** — AC3 hard fail:
  - local008: SQL uses `baseball_batting` → `relation does not exist` (search_path/schema)
  - local022: SQL uses `player_stats` on ipl schema → wrong relation; `warehouse_sql` still null in ToolMessage
- Backend log still shows occasional context BadRequest 44254>40960 (40k non-goal) on overlapping runs; this QA sample pair did not empty-SQL.
