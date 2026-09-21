---
id: inbox-codingland-2026-09-21-github-issue-check-empty-skip
agent: codingland
ticket_id: 2220
updated: 2026-09-21
status: inbox
sources:
  - ticket:2220
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
---

# GH issue check empty skip (codingland 2026-09-21)

- Registry client+extras 전수 `open=0` (gh list + GraphQL OPEN + REST `pull_request==null` + `open_issues_count`).
- Explicit skip: created=0; seal on codingland project #2220 (QA repro path when issues exist: `e2e/scenarios/`).
- Blocker=none; lookback 2026-09-20T23:01Z–2026-09-21T23:01Z.
