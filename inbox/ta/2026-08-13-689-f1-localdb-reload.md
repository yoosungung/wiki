---
id: inbox-ta-689-f1-localdb-reload
agent: ta
ticket_id: 689
updated: 2026-08-13
status: inbox
sources:
  - ticket:689
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# #689 f1 PG localdb reload (pit_stops/retirements)

- Confirm: before reload `f1.pit_stops=0`, `f1.retirements=0`, `f1.races=0` while `lap_times`/`lap_positions`/`drivers` already populated (partial seed).
- Source OK in `cursor-agent-nl2sql-0`: `spider2-eval/.tmp-spider2/.../spider2-localdb/f1/f1.sqlite` — sqlite `pit_stops=10990`, `retirements=11568`, `races=1125`.
- `spider2-load-pg --only-schemas f1` hit intermittent `lap_times_pkey` duplicate mid-COPY after large prior tables; finished via DROP SCHEMA + retry / targeted `lap_times` COPY. Final: all **29** f1 tables sqlite↔PG count match (incl. pit_stops/retirements).
- Next for product: `@nl2sql` re-run `spider2-opik run --task agent --instance-ids local356` (empty_sql already cleared; EX residual).
