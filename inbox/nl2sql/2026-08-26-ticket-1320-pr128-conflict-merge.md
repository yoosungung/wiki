---
id: inbox-nl2sql-1320-pr128-conflict-merge
agent: nl2sql
ticket_id: 1320
updated: 2026-08-26
status: inbox
sources:
  - ticket:1320
  - https://github.com/yoosungung/nl2sql/pull/128
  - wiki/Agents/Text-to-SQL/Stacked-Seal-PR-Conflict-Resolution.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# #1320 PR #128 conflict merge

Sibling seal PRs (#1319/#1321/#1322) landed on main while #128 was CI-wait → `CONFLICTING`/`DIRTY`.

Resolution (no force-push): `merge(main)` in worktree; DESIGN union kept #1320 RCA + main #1321 bullet per Stacked-Seal-PR-Conflict-Resolution.

Evidence: Rust catalog/unparse 10/10; PG seals 2/2. Tip PUT + live SSE still **post-merge** (Metadata-Git-PVC-Resync).
