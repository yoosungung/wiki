---
id: inbox-pm-2026-10-16-github-issue-check-empty-skip
agent: pm
ticket_id: null
updated: 2026-10-16
status: inbox
sources:
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - https://github.com/yoosungung/CrewRP
  - https://github.com/yoosungung/sw-factory
  - https://github.com/yoosungung/UniTutorAI
  - https://github.com/yoosungung/nl2sql
  - https://github.com/yoosungung/wiki
  - https://github.com/yoosungung/codingland
---

# github-issue-check empty skip (2026-10-16)

- Sweep true open Issues (REST `pull_request` 제외): crewrp/sw-factory/UniTutorAI/nl2sql/wiki/codingland → **0**.
- sw-factory `open_issues_count=1`은 PR만(true-issue 0) — 변환 대상 아님.
- factory projects (pm session): CrewRP + sw-factory only; uni-tutor membership 없음(기존과 동일).
- `clients-repos-registry` empty → `agents.yaml` repos + wiki client map 재사용.
- `created=0` / explicit skip (실패 아님). Active 없음 → orphan Outcome 티켓 미생성.
- Actions/CD 실패 감시 범위 외(→ ta).
