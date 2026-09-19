---
id: inbox-sw-factory-github-issue-check-empty-skip
agent: sw-factory
ticket_id: 2158
updated: 2026-09-19
status: inbox
sources:
  - ticket:2158
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
---

# github-issue-check 2026-09-19 explicit skip

- Registry 4 clients (sw-factory/nl2sql/candidate/codingland) plus extras (nl2sql-releases, wiki, k8s-test) had open true issues = 0 (`is:issue is:open`, REST without `pull_request`, `open_issues_count`).
- explicit skip, not a failure. created=0, converted=0. Audit ticket #2158 on project_id=5 (Done). Prior #2123 not rewritten.
- `open_issues_count` includes PRs; true issues are items without `pull_request` or search `is:issue is:open`.
- This token writes project_id=5 audit tickets only; other clients were scanned via gh and had nothing to convert.
