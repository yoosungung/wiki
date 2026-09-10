---
id: inbox-sw-factory-2026-09-10-github-issue-check-empty-skip
agent: sw-factory
ticket_id: 1865
updated: 2026-09-10
status: inbox
sources:
  - ticket:1865
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
---

# github-issue-check 2026-09-10 empty skip

- Client registry (project 5/6/7/8) + extras (nl2sql-releases, wiki, k8s-test): open GH issues = 0.
- Methods: `gh issue list`, REST `pull_request==null`, GraphQL `issues(states:OPEN)`, `open_issues_count`.
- created=0, converted=0 → explicit skip (not failure); audit ticket #1865 Done on project 5.
- Blockers: none.
