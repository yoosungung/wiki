---
id: inbox-pm-2026-08-06-ticket172-pr37-tool-flood-merged
agent: pm
ticket_id: 172
updated: 2026-08-06
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/37
  - https://github.com/yoosungung/nl2sql/actions/runs/30995140476
---

# #172 PR #37 merged — stop FS tool flood

- Eric restored Actions budget (+$10); CI rerun green enough for backend-only merge.
- Merged squash · head `6c7a4dd` · CI at merge: backend pass · mcp-clippy pass (mcp-test/duckdb pending; prior #172 pattern).
- Scope: HarnessProfile exclude FS tools · recursion_limit 40 · analyst_no_sql before done.
- Next: TA redeploy (MDL baseball+ipl already seeded HEAD 5fe07689) → QA smoke → agent-ex 135.
