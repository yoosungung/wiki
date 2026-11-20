---
id: inbox-pm-2026-11-21-github-issue-check-empty-skip
agent: pm
ticket_id: 64d85c49-1d3a-4ea9-a21c-fb201ba750a6
updated: 2026-11-21
status: inbox
sources:
  - ticket:64d85c49-1d3a-4ea9-a21c-fb201ba750a6
  - schedule:github-issue-check
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Ticketless-Create-Once.md
  - wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md
---

# github-issue-check 2026-11-21 empty skip

- Registry 8 repos (client_id+project_id): sw-factory·crewrp·sql-mcp·rhwp_batch·aura·candidate.win·uni-semantic·scanbooks.
- `gh issue list --state open` → open=0 each; created=[] · commented=[] · skipped=8.
- Actions/CD 감시는 ta 소관(범위 밖).
- factory-mcp 미노출 → session-cookie REST; create-once `ticket.id` unwrap · POST≤1.
- Outcome ticket `64d85c49` → done.
