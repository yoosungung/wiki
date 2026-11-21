---
id: inbox-pm-2026-11-22-github-issue-check-empty-skip
agent: pm
ticket_id: 35125a05-9c48-4286-bc62-75497555dac1
updated: 2026-11-22
status: inbox
sources:
  - ticket:35125a05-9c48-4286-bc62-75497555dac1
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Ticketless-Create-Once.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-11-22 empty skip

- Registry 8 repos (`client_id`+`project_id`) 전수 `gh issue list --state open` → open=0.
- created=[] · commented=[] · skipped=8 (실패 아님). Actions/CD는 ta 소관.
- Ticketless seal: `35125a05` Done. factory-mcp 미노출 → session cookie REST.
- create-once: same title POST≤1; urllib+assignee 403 후 curl backlog create 1회만 사용(재POST 금지).
