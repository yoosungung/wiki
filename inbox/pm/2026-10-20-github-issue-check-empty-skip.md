---
id: inbox-pm-2026-10-20-github-issue-check-empty-skip
agent: pm
ticket_id: schedule:github-issue-check
updated: 2026-10-20
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-10-20 empty skip

- `clients-repos-registry` empty → `agents.yaml` repos + wiki client map (sw-factory/crewrp/nl2sql/wiki/UniTutorAI/codingland).
- OPEN true-issue **0** across all (gh list / REST `pr==null` / GQL OPEN). `created=0` / explicit skip.
- sw-factory `open_issues_count=1` = PR#24 only (true-issue 제외).
- factory projects (pm): CrewRP + sw-factory only. `candidate.win` repo 404.
- Active `ticket_id` 없음 → orphan Outcome 미생성. Actions/CD 감시 범위 밖(→ ta).
- Env `GH_TOKEN` invalid; keyring `yoosungung`로 조회.
