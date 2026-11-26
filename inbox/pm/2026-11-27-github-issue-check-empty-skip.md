---
id: inbox-pm-2026-11-27-github-issue-check-empty-skip
agent: pm
ticket_id: 0daa4a78-09c2-4aa2-b519-b20c9de09056
updated: 2026-11-27
status: inbox
sources:
  - ticket:0daa4a78-09c2-4aa2-b519-b20c9de09056
  - wiki/Engineering/AI-Native-Engineering/Github-Issue-Leantime-Intake-Empty-Skip.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
---

# github-issue-check 2026-11-27: open=0 explicit skip

- Registry 8 repos (`client_id`+`project_id` only): all `gh issue list --state open` = 0.
- created=[] · commented=[] · skipped=[sw-factory,crewrp,sql-mcp,rhwp_batch,aura,candidate.win,uni-semantic,scanbooks]
- Dedup N/A; Actions/CD out of scope (ta).
- factory-mcp absent → session.cookie REST; create-once POST≤1 → ticket.id unwrap.
