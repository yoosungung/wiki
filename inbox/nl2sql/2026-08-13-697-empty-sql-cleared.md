---
id: inbox-nl2sql-697-empty-sql-cleared
agent: nl2sql
ticket_id: 697
updated: 2026-08-13
status: inbox
sources:
  - ticket:697
  - ticket:698
  - experiment:local697-empty-sql-residual-tip
  - opik:019ffa39-be73-7d9d-a381-add333dc087b
  - baseline:local690-ipl-after-stash-8fa653a
---

# #697 empty_sql residual cleared (via #698 single-master)

- After #690 stash autofill, local024/229/258 stayed empty_sql — not stash-miss-with-SQL; executes hit `mdl_translation_error: multiple master inner tables` (unjoined `player_match` on `ipl_match_event`).
- #698 tip single-master (`ball_by_ball` only) unblocks execute → #690 stash/SSE can emit warehouse_sql.
- EX `local697-empty-sql-residual-tip`: empty_sql 3→0; local258/229 pass; local024 result_mismatch (out of empty_sql AC).
