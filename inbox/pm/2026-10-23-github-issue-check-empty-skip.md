---
id: inbox-pm-2026-10-23-github-issue-check-empty-skip
agent: pm
ticket_id: df0a706d-cfed-40b9-91a6-dfb76bdd979a
updated: 2026-10-23
status: inbox
sources:
  - schedule:github-issue-check
  - ticket:df0a706d-cfed-40b9-91a6-dfb76bdd979a
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
---

# github-issue-check 2026-10-23 empty skip

- 클라이언트 true-issue open 전수 0 → **created=0 / explicit skip** (실패 아님). 4신호: gh list / REST(pr==null) / GQL OPEN = 0.
- 범위: sw-factory, crewrp, UniTutorAI, codingland, candidate.win, nl2sql. extras: wiki OPEN 0. factory projects: sw-factory / CrewRP.
- sw-factory `open_issues_count=1` = PR #24 only (true issue 0) → skip 확정.
- `clients-repos-registry.json` empty → wiki client map + agents.yaml repos 재사용.
- factory-mcp Cursor namespace 미노출 → session cookie REST fallback. Actions/CD 감시는 ta 소관.
