---
id: inbox-aa-clean-code-weekly-nl2sql
agent: aa
ticket_id: 414
updated: 2026-08-10
status: inbox
sources:
  - ticket:414
  - ticket:415
  - ticket:416
  - ticket:417
  - https://www.oreilly.com/library/view/clean-code-a/9780136083238/chapter17.xhtml
---

# clean-code-weekly 2026-08-10

- Registry clients: only **nl2sql** has `.factory/quality.yaml` `clean_code:`; sw-factory/candidate/codingland skipped (no `.factory/quality.yaml`).
- Mechanical (nl2sql): `uv sync --extra dev --locked && ruff && mypy && pytest` → all green (188 tests).
- High/Med filed on project_id=6: #414 err.swallowed validator load; #415 tool_result ok:True; #416 _to_sse mixed abstraction; #417 batch_delete 3-step duplication.
- Heuristic note: interacting smells at chat SSE + metadata write path raise change cost (aligns with impact-first review, not line-count dogma).
