---
id: inbox-pm-nl2sql-ci-runner-backlog-merge-hold
agent: pm
ticket_id: 1321
updated: 2026-08-26
status: inbox
sources:
  - ticket:1321
  - https://github.com/yoosungung/nl2sql/pull/125
  - https://github.com/yoosungung/nl2sql/actions/runs/32920280981/job/98036482766
---

# nl2sql CI mcp job runner backlog holds Review merges

- 2026-08-26 scoreboard metadata wave: many CI runs queued/in_progress; PR #125 `mcp` job stayed `queued` >35m (job 98036482766) after backend/clippy/mcp-test green.
- Merge gate for Review tickets still requires required checks green — do not merge on partial green while `mcp` pending.
- Symptom of shared runner contention across sibling PRs (#1323/#1324/#1325/#1326/#1327), not a #1321-specific failure.

