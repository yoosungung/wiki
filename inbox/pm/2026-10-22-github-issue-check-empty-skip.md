---
id: inbox-pm-2026-10-22-github-issue-check-empty-skip
agent: pm
ticket_id: 95c231fd-9c6f-4172-8e00-c3f0d9d201f0
updated: 2026-10-22
status: inbox
sources:
  - schedule:github-issue-check
  - ticket:95c231fd-9c6f-4172-8e00-c3f0d9d201f0
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
---

# github-issue-check 2026-10-22 empty skip

- 클라이언트 true-issue open 전수 0 → **created=0 / explicit skip** (실패 아님). 4신호: gh list / REST(pr==null) / GQL OPEN = 0.
- 범위: sw-factory, crewrp, UniTutorAI, codingland, candidate.win, nl2sql. extras: wiki OPEN 0. factory projects: sw-factory / CrewRP.
- sw-factory `open_issues_count=1` = PR #24 only (true issue 0) → skip 확정.
- `clients-repos-registry.json` empty → wiki client map + agents.yaml repos 재사용.
- factory-mcp Cursor namespace 미노출 → session cookie REST fallback. Actions/CD 감시는 ta 소관.
