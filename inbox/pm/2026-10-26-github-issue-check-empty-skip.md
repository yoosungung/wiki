---
id: inbox-pm-2026-10-26-github-issue-check-empty-skip
agent: pm
ticket_id: none
updated: 2026-10-26
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-10-26

- OPEN true-issue 0 → `created=0` explicit skip (실패 아님). 4신호: `gh list` / REST(`pr==null`) / GQL OPEN / search `is:issue is:open`. sw-factory `open_issues_count=1`은 PR#24만.
- Sweep: sw-factory / crewrp / sql-mcp / UniTutorAI / nl2sql / wiki / codingland / candidate.win. Factory ACL: sw-factory, CrewRP, sql-mcp. UniTutorAI project 멤버십 없음(변환 불필요). registry empty → wiki map + agents.yaml.
- Active `ticket_id` 없음 → orphan Outcome/`add_comment` 없음. Actions/CD 감시 범위 밖(ta). factory-mcp namespace 부재 → session-cookie REST fallback. env `GH_TOKEN` 401 → keyring fallback (sweep 성공).
