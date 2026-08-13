---
id: inbox-nl2sql-691-ipl-wicket-player-id
agent: nl2sql
ticket_id: 691
updated: 2026-08-13
status: inbox
sources:
  - ticket:691
  - spider2-eval/DESIGN.md
  - mcp/tests/search_ipl_wicket_taken_catalog.rs
---

# #691 IPL ipl_wicket_taken.player_id := player_out

- Scoreboard local259 failed: `GROUP BY ipl_wicket_taken.player_id` but warehouse subquery only exposed `player_out` (PG hint).
- Fix: tip+fixture model `ipl_wicket_taken` with physical `player_id` from `m.player_out` (+ `kind_out`); relation to `ipl_player`. `ipl_match_event.player_out` description distinguishes bowler `player_id`.
- local228 sql_exec syntax-at-end was unbalanced paren in agent SQL (catalog OK) — agent residual, not MDL.
