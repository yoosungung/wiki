---
id: inbox-pm-2026-11-25-github-issue-check-empty-skip
agent: pm
ticket_id: null
updated: 2026-11-25
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
---

# github-issue-check empty skip (2026-11-25)

- Registry `.cursor/github-issues-registry.json`: 8 repos with `client_id`+`project_id` (sw-factory, crewrp, sql-mcp, rhwp_batch, aura, candidate.win, uni-semantic, scanbooks).
- `gh issue list --state open` all 8 → `[]` (PRs/Actions out of scope; ta owns CD fail watch).
- created=0 · commented=0 · skipped remaining=0 · no new tickets · ticketless → no orphan Outcome.
