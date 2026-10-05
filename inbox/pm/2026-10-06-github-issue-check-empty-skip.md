---
id: inbox-pm-2026-10-06-github-issue-check-empty-skip
agent: pm
ticket_id: null
updated: 2026-10-06
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-10-06 empty skip

- `clients-repos-registry.json` empty → wiki client map + `agents.yaml` repos 재사용.
- factory projects: sw-factory / CrewRP / UniTutorAI (nl2sql project 없음).
- Sweep OPEN true-issue **0** → `created=0` / explicit skip (실패 아님).
  - sw-factory: gh list 0 · REST(pr==null) 0 · GQL OPEN 0 · search is:issue 0; `open_issues_count=1` = PR#24 only.
  - crewrp / UniTutorAI / wiki: 4신호 모두 0.
  - nl2sql: issues ACL/token 403 → `open_issues_count=0`만 확인 · 변환 티켓 미생성.
- Active `ticket_id` 없음 → orphan Outcome 티켓 미생성.
- Actions/CD 실패 감시 범위 아님(→ ta).
