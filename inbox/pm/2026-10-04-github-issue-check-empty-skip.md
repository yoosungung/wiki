---
id: inbox-pm-2026-10-04-github-issue-check-empty-skip
agent: pm
ticket_id: null
updated: 2026-10-04
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-10-04: open=0 explicit skip

- Outcome: `created=0` / **explicit skip** (실패 아님). Active `ticket_id` 없음 → orphan Outcome 티켓 미생성.
- Registry: pm `clients-repos-registry` empty → `agents.yaml` repos + wiki client map 재사용.
- Factory projects: sw-factory / CrewRP / UniTutorAI. Actions/CD 감시 범위 밖(→ ta).

## Sweep (true issues; PRs excluded)

| repo | gh list | REST(pr==null) | GQL OPEN | open_issues_count |
|------|---------|----------------|----------|-------------------|
| yoosungung/sw-factory | 0 | 0 | 0 | 1 (PR#24 only) |
| yoosungung/crewrp | 0 | 0 | 0 | 0 |
| yoosungung/UniTutorAI | 0 | 0 | 0 | 0 |
| yoosungung/wiki | 0 | 0 | 0 | 0 |
| yoosungung/nl2sql | blocked | 403 | FORBIDDEN | 0 |

- nl2sql issues ACL/token 403: `open_issues_count=0`만 확인; 변환 티켓 미생성.
- Dedup 마커 불필요(신규 true-issue 0).
