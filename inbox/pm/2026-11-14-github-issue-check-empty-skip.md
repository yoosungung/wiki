---
id: inbox-pm-2026-11-14-github-issue-check-empty-skip
agent: pm
ticket_id: none
updated: 2026-11-14
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check empty skip 2026-11-14

- Registry `.cursor/github-issues-registry.json` repos=7 (sw-factory, crewrp, sql-mcp, rhwp_batch, aura, candidate.win, uni-semantic); all have client_id+project_id.
- `gh issue list --state open --limit 50` → all `[]`; spot-check `open_issues_count=0` for all 7.
- Outcome: `created=0` / `commented=0` / `skipped=empty-open` (7 repos). Actions/CD out of scope (ta).
- factory-mcp Cursor namespace absent → session-cookie REST membership probe 7×200.
- No Active ticket_id → orphan Outcome 미생성.
