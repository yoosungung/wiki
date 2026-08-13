---
id: inbox-nl2sql-698-ipl-single-master
agent: nl2sql
ticket_id: 698
updated: 2026-08-13
status: inbox
sources:
  - ticket:698
  - experiment:local698-ipl-single-master
  - opik:019ffa25-d35e-7171-bd07-9a8aecf2ea93
  - tip-mdl:a9b5a749
---

# #698 ipl_match_event single master (result_mismatch)

- Root cause: tip `ipl_match_event` unjoined `player_match` → `mdl_translation_error: multiple master inner tables (2)`; stash emitted exploratory SQL after #690 autofill.
- Fix: drop `player_match`; master=`ball_by_ball` only; `player_id`:=`bowler` for relation. Fixture+`search_ipl_bowling_catalog` regression.
- EX `local698-ipl-single-master`: pass_rate 0.333 — local020 pass; local023 batting_average (Dhawan 47.4 vs gold 40.6 = non-striker run-outs); local025 6/568 over picks + missing bowler_name (avg 19.400 vs 19.426).
