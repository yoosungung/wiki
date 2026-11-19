---
id: inbox-pm-2026-11-20-github-issue-check-empty-skip
agent: pm
ticket_id: 396a8a18-12e4-4937-9857-9b5eff4eb948
updated: 2026-11-20
status: inbox
sources:
  - ticket:396a8a18-12e4-4937-9857-9b5eff4eb948
  - schedule:github-issue-check
  - .cursor/github-issues-registry.json
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Ticketless-Create-Once.md
---

# github-issue-check 2026-11-20 empty skip

- Registry 8 repos (client_id+project_id): sw-factory · crewrp · sql-mcp · rhwp_batch · aura · candidate.win · uni-semantic · scanbooks.
- `gh issue list --state open` each → open=0; created=[] · commented=[] · skipped=8 (실패 아님).
- Actions/CD 감시 범위 밖(ta). factory-mcp 미노출 → REST+session.cookie create-once Outcome.
- Canonical already covers empty-skip: Factory-Schedule-Ops-Skips / Github-Issue-Leantime-Intake-Empty-Skip.
