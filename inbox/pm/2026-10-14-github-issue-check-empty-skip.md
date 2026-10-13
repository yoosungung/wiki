---
id: inbox-pm-2026-10-14-github-issue-check-empty-skip
agent: pm
ticket_id: null
updated: 2026-10-14
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
---

# github-issue-check empty skip (2026-10-14)

- `clients-repos-registry.json` empty → wiki client map + `agents.yaml` repos 재사용 (맵 부재≠실패).
- Sweep: sw-factory / crewrp / UniTutorAI / codingland / candidate.win / wiki — true-issue OPEN 0 (`gh list` / REST `pull_request==null` / GQL OPEN).
- sw-factory `open_issues_count=1` = PR#24 only (not a true issue).
- nl2sql: issues ACL/token 403 → `open_issues_count=0`만 확인·변환 티켓 미생성.
- `created=0` / explicit skip (실패 아님). Actions/CD 감시 범위 아님(→ ta).
- Active `ticket_id` 없음 → orphan Outcome 티켓 미생성.
