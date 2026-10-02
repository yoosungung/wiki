---
id: inbox-pm-2026-10-03-github-issue-check-empty-skip
agent: pm
ticket_id: none
updated: 2026-10-03
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check empty skip (2026-10-03)

- `clients-repos-registry.json` empty → wiki 맵 + `agents.yaml` repos 재사용 (맵 부재≠실패).
- factory projects: `sw-factory`, `CrewRP`, `UniTutorAI` (nl2sql 프로젝트 없음).
- Sweep true-issue OPEN=0 → `created=0` / **explicit skip** (실패 아님). Actions/CD 미감시(ta).

| repo | gh list | REST(pr==null) | GQL issues OPEN | open_issues_count | note |
|------|---------|----------------|-----------------|-------------------|------|
| yoosungung/sw-factory | 0 | 0 | 0 | 1 | PR#24만 open |
| yoosungung/crewrp | 0 | 0 | 0 | 0 | |
| yoosungung/UniTutorAI | 0 | 0 | 0 | 0 | |
| yoosungung/wiki | 0 | 0 | 0 | 0 | extras |
| yoosungung/codingland | — | — | — | 0 | legacy map |
| berryking404/candidate.win | — | — | — | 0 | legacy map |
| yoosungung/nl2sql | 403 | 403 | — | 0 | issues ACL; count만 확인 |

- Active `ticket_id` 없음 → Outcome/감사 티켓 orphan 생성 금지.
- factory-mcp 네임스페이스 미로드 → REST 세션(`pm@example.com`)으로 projects만 확인.
