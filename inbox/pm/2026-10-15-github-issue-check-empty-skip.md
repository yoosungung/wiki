---
id: inbox-pm-2026-10-15-github-issue-check-empty-skip
agent: pm
ticket_id: schedule:github-issue-check
updated: 2026-10-15
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check empty skip (2026-10-15)

- `clients-repos-registry.json` empty → agents.yaml repos + wiki client map 재사용 (맵 부재≠실패).
- factory projects (pm session): `sw-factory`, `CrewRP` only (uni-tutor membership 없음).
- Sweep OPEN true-issue **0** → `created=0` / explicit skip (실패 아님).
  - sw-factory: gh/REST/GQL=0; `open_issues_count=1`은 PR만 (true-issue 제외).
  - CrewRP / UniTutorAI / codingland / wiki / berryking404/candidate.win: 4신호 0.
  - nl2sql: `open_issues_count=0`; issues list ACL/token 403 → 변환 티켓 미생성.
- Active `ticket_id` 없음 → orphan Outcome 미생성.
- Actions/CD 실패 감시 범위 아님 (→ ta).
