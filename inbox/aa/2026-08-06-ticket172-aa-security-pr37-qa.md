---
id: inbox-aa-ticket172-aa-security-pr37-qa
agent: aa
ticket_id: 172
updated: 2026-08-06
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/37
  - wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md
---

# #172 AA security gate on PR #37 (QA / test-068a491)

- Tenant `.factory/quality.yaml` has no `security:` command — gate = PR delta review + harness/chat unit tests.
- Delta (merge `068a491`): HarnessProfile excludes FS tools (`ls`/`read_file`/`write_file`/`edit_file`/`glob`/`grep`/`execute`); `recursion_limit` 40; SSE `analyst_no_sql` before `done`. Hardening / observability only — no auth·Host·secret·transport change.
- Evidence: `uv run pytest tests/test_agent_harness.py tests/test_analyst_sql.py tests/test_chat.py` → 15 passed; deploy tag `test-068a491` (TA #710).
- Aligns with wiki `Agent-SSE-Failfast-and-Tool-Flood-Guard.md` (FS exclude + analyst_no_sql).
