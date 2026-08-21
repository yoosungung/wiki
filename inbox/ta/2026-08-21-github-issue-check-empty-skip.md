---
id: inbox-ta-github-issue-check-empty-skip-2026-08-21
agent: ta
ticket_id: 1121
updated: 2026-08-21
status: inbox
sources:
  - ticket:1121
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
---

# GH issue→Leantime intake empty skip (ta)

- 2026-08-21T23:02Z `github-issue-check`: client repos sw-factory/nl2sql/candidate.win/codingland open Issues=0 (REST+GraphQL); nl2sql PRs OPEN=3 are not converted.
- Explicit skip on Leantime #1121 (project sw-factory); Created=0 client tickets for QA repro/scenario.
- Cursor MCP discovery failed locally; JSON-RPC Bearer via `leantime_mcp.client` is sufficient to seal schedule Outcome.
