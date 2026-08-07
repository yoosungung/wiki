---
id: inbox-pm-github-issue-check-skip-2026-08-07
agent: pm
ticket_id: 317
updated: 2026-08-07
status: inbox
sources:
  - ticket:317
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
---

# github-issue-check 2026-08-07 empty skip

- clients-repos scan (nl2sql/codingland/candidate.win/sw-factory): `gh issue list --state open` = 0 → explicit skip, no convert tickets.
- Dedup marker for future converts: `<!-- github:owner/repo#N -->` on matching client project.
- Blockers: none. Outcome on Leantime #317 (sw-factory project 5).
