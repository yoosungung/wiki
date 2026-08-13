---
id: inbox-nl2sql-689-f1-pit-reload-lap-type-mdl
agent: nl2sql
ticket_id: 689
updated: 2026-08-13
status: inbox
sources:
  - ticket:689
  - inbox/nl2sql/2026-08-13-689-local356-tip-apply-ex.md
  - spider2-eval/DESIGN.md
---

# #689 PG f1 pit reload + lap_type pairwise MDL

- Confirmed `f1.pit_stops`/`retirements` were 0; `spider2-localdb` missing until `local_sqlite.zip` (gdrive `1coEVsCZq-Xvj9p2TnhBFoFTsY-UoYGmG`) unzipped.
- `spider2-load-pg --only-schemas f1` failed on `liveries.end_year` NOT NULL (PK); surgical restore via Python `TRUNCATE ONLY` + `session_replication_role=replica` → `pit_stops=10990`, `retirements=11568`, `lap_times=575029`, `lap_positions=613112`.
- Boy Scout MDL: pairwise on-track + `lap_type` Race/Starting Position/Retirement guidance on tip+fixtures; search regression +1.
- local356 after data+MDL still `pass_rate 0` (agent SQL rewrite out of PM scope unless Eric expands).
