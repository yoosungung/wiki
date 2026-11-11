---
id: inbox-pm-2026-11-12-github-issue-check-empty-skip
agent: pm
ticket_id: N/A — ticketless schedule (orphan Outcome 금지)
updated: 2026-11-12
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-11-12 empty skip

- Registry `.cursor/github-issues-registry.json` repos with client_id+project_id = 7: sw-factory, crewrp, sql-mcp, rhwp_batch, aura, candidate.win, uni-semantic.
- `gh issue list --state open --limit 50` (true issues; PRs excluded) → all open=0.
- Spot-check `open_issues_count`: sw-factory/candidate.win/uni-semantic = 0 (PR-only 잔여 없음).
- Outcome: created=0 · commented=0 · skipped=empty-open (실패 아님).
- No Active ticket_id → orphan Outcome 미생성 (Schedule-Outcome-Requires-Active-Ticket).
- Actions/CD 실패 감시 범위 밖(ta). factory-mcp Cursor namespace 미노출 → session-cookie REST search/probe only.
