---
id: inbox-pm-2026-08-13-564-pr77-career-sum-merge
agent: pm
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - https://github.com/yoosungung/nl2sql/pull/77
---

# #564 PM merged nl2sql#77 (career SUM + search diversity)

- Trigger: QA mention (delegated_from=5 · delegated_to=2) + nl2sql #3193 Review handoff.
- Prior tip test-500a8c6 AC2: empty_sql=0 · pass_rate=0 · result mismatch (local008 season MAX vs career SUM).
- PR #77 scope: MCP token-coverage diversity · search k 3/4 · analyst career SUM + stop-after-scorable; CI backend/mcp-clippy/mcp-test/mcp all SUCCESS.
- Merged: merge_sha 7f519f23184071c098ee50ded2b8a2713fba978b · board → Deploying Test @ta for tip roll past test-500a8c6 → QA AC2. Not Deploying Prod.
