---
id: inbox-nl2sql-690-ipl-ball-key-joins
agent: nl2sql
ticket_id: 690
updated: 2026-08-13
status: inbox
sources:
  - ticket:690
  - spider2-eval/DESIGN.md
  - mcp/tests/search_ipl_bowling_catalog.rs
---

# #690 IPL ipl_match_event ball-key joins + bowling vocab

- Tip `ipl_match_event` had `batsman_scored`/`extra_runs`/`wicket_taken` joins `ball_id`→`match_id` (wrong). Gold/local023 join is `match_id+over_id+ball_id+innings_no`.
- Boy Scout: composite ball-key joins + bowling average/economy/partnership/`kind_out` descriptions; fixture+`search_ipl_bowling_catalog` regression.
- Cluster DBs: IPL (6) + Baseball local007 (career debut/final_game) — Baseball not in this MDL slice.
