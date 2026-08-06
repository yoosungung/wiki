---
id: inbox-aa-ticket172-aa-security-pr38-qa
agent: aa
ticket_id: 172
updated: 2026-08-06
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/38
---

# #172 aa security pass on test-841059f (PR #38)

- `.factory/quality.yaml` has no `security:` command → delta review + unit evidence (same pattern as #711).
- Delta: `slim_search_for_llm` tighter caps (columns≤20, relations≤8; drop valueDomain/expression fluff). Data minimization only; no auth·Host·secret·transport change.
- Tests: `pytest tests/test_agent_tool_payload.py tests/test_agent_harness.py tests/test_analyst_sql.py tests/test_chat.py` → pass on sha `841059f`.
- Live: `ghcr.io/yoosungung/nl2sql-backend:test-841059f` health/ready 200 (TA #734).
