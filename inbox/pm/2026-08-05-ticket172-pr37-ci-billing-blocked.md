---
id: inbox-pm-2026-08-05-ticket172-pr37-ci-billing-blocked
agent: pm
ticket_id: 172
updated: 2026-08-05
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/37
  - https://github.com/yoosungung/nl2sql/actions/runs/30995140476
---

# #172 PR #37 CI blocked — GH Actions billing

- PR #37 OPEN · MERGEABLE · head `6c7a4dd` (FS tool exclude + analyst_no_sql).
- Local: `pytest tests/test_chat.py tests/test_analyst_sql.py tests/test_agent_harness.py` → 15 passed.
- CI run 30995140476: all jobs fail in ~2s — annotation: account payments failed / spending limit (jobs never started).
- Merge held until billing unblocked; then re-run checks → merge → TA redeploy.
