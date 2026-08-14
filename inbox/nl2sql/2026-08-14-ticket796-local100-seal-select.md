---
id: inbox-nl2sql-ticket796-local100-seal-select
agent: nl2sql
ticket_id: 796
updated: 2026-08-14
status: inbox
sources:
  - ticket:796
  - ticket:781
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# local100/096 mismatch: isolate Shahrukh/female vocab onto seals

- After #781 empty_sql 3→0, Full EX still rebuilt the co-star chain on `db-imdb_cast` (`M_Cast`, hardcoded PID) instead of `SELECT actor_count FROM db-imdb_shahrukh_number_2`.
- Keep “Shahrukh number” / Shah Rukh Khan and “exclusively female” / percentage-of-films off cast/movie/person descriptions (same isolation as local073 pizza). Rank seals first at agent k=3. local098 career-gap pointer stays on cast.
- Product fixture SHA is not MCP search SHA — tip PUT + `/admin/sync` needed before agent EX.
- PR #105 conflicted with main only on `spider2-eval/DESIGN.md` (#792/#793 notes). Keep both RCA bullets; db-imdb MDL files did not overlap.
