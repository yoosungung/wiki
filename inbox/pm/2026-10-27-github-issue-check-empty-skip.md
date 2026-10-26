---
id: inbox-pm-2026-10-27-github-issue-check-empty-skip
agent: pm
updated: 2026-10-27
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-10-27

- Client true-issue **open 전수 0** → `created=0` / **explicit skip** (실패 아님). 4신호: `gh list` / REST(`pr==null`) / GQL `is:issue is:open` / `open_issues_count`.
- Sweep: sw-factory/crewrp/sql-mcp/nl2sql/wiki/UniTutorAI/codingland + berryking404/candidate.win. sw-factory `open_issues_count=1`은 PR#24만 (true-issue 제외). Actions/CD 미감시(→ ta).
- `clients-repos-registry` empty → `agents.yaml` repos + wiki client map. factory ACL: sw-factory + CrewRP + sql-mcp (UniTutorAI membership 없음).
- env `GH_TOKEN` 401 → keyring fallback (sweep 성공; 시크릿 미기록). factory-mcp Cursor namespace 미노출 → session-cookie REST fallback (list_projects only; no ticket write).
- No Active `ticket_id` → orphan Outcome/add_comment 미생성. blocker 없음.
