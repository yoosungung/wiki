---
id: inbox-nl2sql-ticket685-local022-striker
agent: nl2sql
ticket_id: 685
updated: 2026-08-13
status: inbox
sources:
  - ticket:685
  - ticket:683
  - ticket:564
  - https://github.com/yoosungung/nl2sql/pull/79
---

# #685 local022 EX: batsman_scored needs ball_by_ball.striker

- Gold local022 = 7 player names. `ipl.batsman_scored` has no player_id; runs must join `ball_by_ball` on ball keys to `striker`.
- Failure SQL joins `batsman_scored` only to `player_match`/`match` → ~447 names (team-wide duplication). `team_id <> match_winner` + striker join matches gold.
- Tip SSE often ends with exploratory `SELECT * FROM ipl_player_match` then striker-less rewrite as last sql.
- Fix: analyst prompt TDD (`test_analyst_prompt_ipl_striker`) + PR #79; tip agent re-gate pending tip roll.
