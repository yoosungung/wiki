---
id: inbox-pm-ticket391-pr54-mypy-bounce
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/54
---

# #391 PR #54 Review bounce — mypy ToolCall typing

- Scope OK vs SoT 1792 (empty `task({})` + silent stop → analyst).
- CI blocker: backend Mypy on `task_guard.py:145/148` — `list[dict[str, Any]]` vs `list[ToolCall]`.
- Board: bounced In Progress/@nl2sql; merge deferred until mypy+CI green.
