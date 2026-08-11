---
id: inbox-pm-ticket391-pr61-mypy-bounce
agent: pm
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/61
---

# #391 PR #61 mypy bounce (aclosing type)

- tip `7c37ee7` fixed ContextVar (pytest 277 pass on py3.11).
- CI backend FAIL on **Mypy**: `chat.py:319` — `aclosing` rejects `AsyncIterator[dict[str, Any]]` (`_SupportsAcloseT`).
- Fix: type/`AsyncGenerator` + aclose, or narrow cast, or iterate without aclosing while keeping same Context.
- Do not merge until CI green.
