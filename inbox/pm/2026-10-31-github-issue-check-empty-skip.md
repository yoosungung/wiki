---
id: inbox-pm-2026-10-31-github-issue-check-empty-skip
agent: pm
updated: 2026-10-31
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-10-31 explicit skip

- `clients-repos-registry` empty → wiki client map + `agents.yaml` repos. Sweep: sw-factory/crewrp/sql-mcp/nl2sql/wiki/UniTutorAI/codingland/candidate.win.
- 4-signal: `gh list` / REST(`pr==null`) / GQL OPEN true-issue **0** all repos. sw-factory `open_issues_count=1` is PR#24 only (`is:issue is:open`=0). `created=0` explicit skip (not a failure).
- factory projects (pm cookie REST): sw-factory, CrewRP, sql-mcp. UniTutorAI membership absent. No new conversion tickets. Actions/CD out of scope (→ ta).
- No Active `ticket_id` → no orphan Outcome comment. factory-mcp Cursor namespace absent; session-cookie REST fallback (read-only). env `GH_TOKEN` 401 → keyring fallback (시크릿 미기록).
