---
id: inbox-pm-2026-11-26-github-issue-check-empty-skip
agent: pm
ticket_id: 4f2ca567-f756-428c-95d1-1b538aea10a0
updated: 2026-11-26
status: inbox
sources:
  - ticket:4f2ca567-f756-428c-95d1-1b538aea10a0
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
---

# github-issue-check 2026-11-26 empty skip

- Registry 8 repos (`client_id`+`project_id`); `gh issue list --state open` → open=0 each.
- Outcome: created=0 · commented=0 · skipped=8 (explicit skip, not failure).
- Actions/CD 감시 범위 밖(ta). factory-mcp 부재 → session.cookie REST create-once (`ticket.id`, POST≤1).
