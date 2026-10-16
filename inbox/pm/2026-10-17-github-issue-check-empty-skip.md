---
id: inbox-pm-2026-10-17-github-issue-check-empty-skip
agent: pm
ticket_id: none
updated: 2026-10-17
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check empty skip (2026-10-17)

- `clients-repos-registry` empty → `agents.yaml` repos + wiki extras 재사용 (맵 부재≠실패).
- Sweep OPEN true-issue **0** → `created=0` / explicit skip (실패 아님). Actions/CD 감시 제외(→ ta).
- Repos: sw-factory, crewrp, nl2sql, wiki, UniTutorAI, codingland, candidate.win.
- 4신호: `gh issue list` / REST(`pull_request==null`) / GQL OPEN / `open_issues_count` — true-issue 전부 0.
- sw-factory `open_issues_count=1`은 PR#24만 (`gateway: manual_prompt → deliverTicketless`); true-issue 아님.
- factory projects visible to pm: CrewRP, sw-factory. Active `ticket_id` 없음 → orphan Outcome 미생성.
- blocker add_comment: N/A (변환 대상·기존 블로커 없음).
