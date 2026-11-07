---
id: inbox-pm-2026-11-08-github-issue-check-empty-skip
agent: pm
ticket_id: N/A
updated: 2026-11-08
status: inbox
sources:
  - schedule:github-issue-check
  - .cursor/github-issues-registry.json
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-11-08 empty skip

- Registry repos (client_id+project_id): sw-factory, crewrp, sql-mcp, rhwp_batch, aura, candidate.win (6).
- factory-mcp Cursor namespace absent → session-cookie REST project probe only (all 6 memberships 200).
- GH: env `GH_TOKEN` OK; `gh` binary absent → REST `GET /repos/{owner}/{repo}/issues?state=open` + filter `pull_request==null`.
- OPEN true-issue = 0 across all 6 → `created=0` / `commented=0` / `skipped=empty-open`.
- Actions/CD 감시 out of scope (ta). No Active ticket_id → orphan Outcome 미생성.
- at: 2026-11-07T23:00Z (KST 2026-11-08)
