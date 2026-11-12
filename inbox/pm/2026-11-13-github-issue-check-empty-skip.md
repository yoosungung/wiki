---
id: inbox-pm-2026-11-13-github-issue-check-empty-skip
agent: pm
ticket_id: null
updated: 2026-11-13
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-11-13 empty-open skip

- Registry `.cursor/github-issues-registry.json` repos with `client_id`+`project_id`: sw-factory, crewrp, sql-mcp, rhwp_batch, aura, candidate.win, uni-semantic (7).
- `gh issue list --state open` all 0 → `created=0` / `commented=0` / `skipped=empty-open`.
- Spot-check `open_issues_count`: sw-factory/candidate.win/uni-semantic = 0.
- factory-mcp Cursor namespace absent → session-cookie REST (`/api/projects` 200, 7 projects). Ticketless → orphan Outcome 금지.
- Actions/CD 감시 out of scope (→ ta).
