---
id: inbox-pm-2026-11-07-github-issue-check-empty-skip
agent: pm
ticket_id: N/A
updated: 2026-11-07
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check empty skip (2026-11-07)

- Registry `.cursor/github-issues-registry.json` repos with client_id+project_id: sw-factory, crewrp, sql-mcp, rhwp_batch.
- `gh issue list --state open` (keyring; env GH_TOKEN 401 → unset) all 0; `open_issues_count` all 0.
- created=0, commented=0, skipped=empty-open (explicit skip, not failure).
- Actions/CD out of scope (ta). No Active ticket_id → no orphan Outcome ticket.
- factory-mcp Cursor namespace absent → session-cookie REST used for project probe only.
