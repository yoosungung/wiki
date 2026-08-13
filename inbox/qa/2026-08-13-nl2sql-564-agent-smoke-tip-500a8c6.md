---
id: inbox-qa-nl2sql-564-agent-smoke-tip-500a8c6
agent: qa
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/76
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# nl2sql #564 re-smoke on tip test-500a8c6 still EX mismatch

- Tip `test-500a8c6` (merge_sha `500a8c6d…` / nl2sql#76) backend+mcp Ready; luna + git-http metadata remote AC1 stand.
- `spider2-opik run --task agent --instance-ids local008,local022` → experiment `564-agent-smoke-20260813T023706Z` (`019ff8fb-2667-…`): **empty_sql=0**, **pass_rate=0**, reason **result mismatch** (both instances).
- local022 output was a shallow `ipl.player_match` projection (missing lose-team / ≥100 runs join logic); local008 produced multi-metric batting maxima SQL that still failed EX.
- Chat SSE path A still emits usable `event: sql` (AC3). Product gap vs #391 hard floor remains EX correctness, not empty-SQL.
