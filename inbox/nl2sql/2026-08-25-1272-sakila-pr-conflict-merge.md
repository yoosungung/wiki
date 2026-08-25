---
id: inbox-nl2sql-1272-sakila-pr-conflict-merge
agent: nl2sql
ticket_id: 1272
updated: 2026-08-25
status: inbox
sources:
  - ticket:1272
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# PR conflict after stacked seal merge (#1272)

- Scoreboard seal PRs that branch from a sibling feature tip (not main) conflict when the sibling merges first (#119 then #121).
- Prefer `merge(main)` over rebase when force-push is forbidden; resolve DESIGN.md by keeping all ticket bullets in numeric order.
- Stacked commits (e.g. #1271 on #1272 branch) remain in the PR after merge-main — note for PM merge-order vs sibling PR.
