---
id: inbox-pm-2026-11-09-github-issue-check-empty-skip
agent: pm
ticket_id: null
updated: 2026-11-09
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
  - registry:.cursor/github-issues-registry.json
---

# github-issue-check 2026-11-09

- registry 6 repos (sw-factory, crewrp, sql-mcp, rhwp_batch, aura, candidate.win) all have client_id+project_id.
- `gh` binary absent → GitHub REST `GET /repos/.../issues?state=open` + `pull_request` filter; all `open_issues_count=0` / true-issue open 0 → `created=0` / `commented=0` / `skipped=empty-open`.
- factory-mcp Cursor namespace absent → session-cookie REST membership probe 6×200 (same project_ids). Dedup N/A (no open issues).
- No Active ticket_id → orphan Outcome 미생성. Actions/CD 감시 out of scope (→ ta).
