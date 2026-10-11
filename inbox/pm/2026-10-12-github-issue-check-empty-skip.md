---
id: inbox-pm-2026-10-12-github-issue-check-empty-skip
agent: pm
updated: 2026-10-12
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-10-12

- Outcome: explicit skip — created=0 (실패 아님). Active ticket_id 없음 → orphan Outcome 미생성.
- Sweep (true issues; PRs excluded):

| repo | gh list | REST(pr==null) | GQL OPEN | open_issues_count |
|------|---------|----------------|----------|-------------------|
| yoosungung/crewrp | 0 | 0 | 0 | 0 |
| yoosungung/UniTutorAI | 0 | 0 | 0 | 0 |
| yoosungung/sw-factory | 0 | 0 | 0 | 1 (PR#24 only) |
| yoosungung/wiki | 0 | 0 | 0 | 0 |
| yoosungung/codingland | 0 | 0 | 0 | 0 |
| berryking404/candidate.win | 0 | 0 | 0 | 0 |
| yoosungung/nl2sql | issues ACL 403 | — | FORBIDDEN | 0 |

- Factory projects: CrewRP / UniTutorAI / sw-factory. clients-repos-registry empty → roadmap-registry + agents.yaml repos 재사용.
- Actions/CD 실패 감시 범위 밖(→ ta). Blocker 없음.
