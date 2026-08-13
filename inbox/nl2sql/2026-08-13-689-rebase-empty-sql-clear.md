---
id: inbox-nl2sql-689-rebase-empty-sql-clear
agent: nl2sql
ticket_id: 689
updated: 2026-08-13
status: inbox
sources:
  - ticket:689
  - https://github.com/yoosungung/nl2sql/pull/84
  - experiment:local356-689-pairwise-shape
---

# #689 rebase + empty-SQL clear; EX mismatch remains

- Rebased PR#84 onto main (kept #690 IPL bullet + #689 F1); mergeable again.
- ForceExecute now sets `response_format=None` — local EX no longer empty SQL.
- `local356-689-pairwise-shape`: SQL emitted with `lap_position` pairwise but **result mismatch** (pass_rate 0). Tip still needs Kaniko roll of head for cluster EX.
