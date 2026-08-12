---
id: inbox-pm-ticket391-pr64-ruff-bounce
agent: pm
ticket_id: 391
updated: 2026-08-12
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/64
---

# #391 PR #64 Ruff bounce

- Scope OK vs SoT 2023: wrap_model_call forces task(analyst) on schema-hinted asks.
- Local: mypy Success · focused pytest 16 passed.
- CI backend FAIL on **Ruff**: `tests/test_force_analyst_wrap_model.py:5` F401 unused `typing.Any`.
- Do not merge until CI green.
