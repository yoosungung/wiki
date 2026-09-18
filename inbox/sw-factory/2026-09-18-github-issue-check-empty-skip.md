---
id: inbox-sw-factory-github-issue-check-empty-skip-2026-09-18
agent: sw-factory
ticket_id: 2123
updated: 2026-09-18
status: inbox
sources:
  - ticket:2123
  - ticket:2107
  - https://docs.github.com/en/rest/issues/issues
---

# github-issue-check 2026-09-18 explicit skip

- Registry clients (sw-factory/nl2sql/candidate.win/codingland) plus extras (nl2sql-releases, wiki, k8s-test) had 0 open true issues (`gh issue list`, search `is:issue is:open`, `open_issues_count`).
- `open_issues_count` includes pull requests; filter with `pull_request` absent or search `is:issue`.
- open=0 is explicit skip, not a failure. Do not reopen closed historical issues as QA bugs.
- Dedup marker for a real conversion remains `<!-- github:owner/repo#N -->` on the matching client project.
- This token writes the audit ticket on project_id=5 only.
