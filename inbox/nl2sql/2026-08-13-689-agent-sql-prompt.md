---
id: inbox-nl2sql-689-agent-sql-prompt
agent: nl2sql
ticket_id: 689
updated: 2026-08-13
status: inbox
sources:
  - ticket:689
  - https://github.com/yoosungung/nl2sql/pull/84
---

# #689 agent-SQL pairwise prompt (EX still open)

- Eric (B): analyst prompt for pairwise `f1_lap.lap_position` + pit/retirement exclusions (not LAG-only).
- TDD: `backend/tests/test_analyst_prompt_f1_overtake.py`.
- Tip Kaniko blocked here (`nl2sql-ghcr-build` Secret forbidden); tip image still `test-ad563ae`.
- Local EX (`local356-689-prompt-v4`) still pass_rate 0 — empty SQL (agent skipped `execute_select_query` / AnalystResponse validation).
