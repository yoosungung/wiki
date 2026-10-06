---
id: inbox-pm-2026-10-07-github-issue-check-empty-skip
agent: pm
ticket_id: N/A
updated: 2026-10-07
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-10-07 explicit skip

- clients-repos-registry empty → agents.yaml repos + factory projects (sw-factory / CrewRP / UniTutorAI) + wiki extras.
- **sw-factory** (`yoosungung/sw-factory`): gh list=0, REST true=0, GQL OPEN=0; `open_issues_count=1` = PR#24 only (not true issue).
- **crewrp** / **UniTutorAI** / **wiki**: 4신호 all 0.
- **nl2sql**: issues ACL/token 403; `open_issues_count=0`만 확인 → 변환 티켓 미생성.
- created=0 / explicit skip (실패 아님). Actions/CD 감시 범위 아님(→ ta).
- Active ticket_id 없음 → orphan Outcome 미생성.
