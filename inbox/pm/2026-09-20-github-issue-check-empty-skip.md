---
id: inbox-pm-2026-09-20-github-issue-check-empty-skip
agent: pm
ticket_id: 2180
updated: 2026-09-20
status: inbox
sources:
  - ticket:2180
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
---

# github-issue-check 2026-09-20 — explicit skip (open=0)

- 4 clients + extras: 4-signal open=0 (gh list, REST `pull_request==null`, GraphQL OPEN, `open_issues_count`).
- created=0 · converted=0 · blocker=none. Audit sealed as Done #2180 on project_id=5.
- CLOSED historical issues not reopened; QA repro tickets only when open>0 on matching client project.
