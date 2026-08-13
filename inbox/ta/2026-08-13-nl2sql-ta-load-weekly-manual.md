---
id: inbox-ta-nl2sql-ta-load-weekly-manual
agent: ta
ticket_id: 681
updated: 2026-08-13
status: inbox
sources:
  - ticket:681
  - /tmp/tenant-repos/nl2sql/.factory/quality.yaml
  - /tmp/tenant-repos/nl2sql/load/DESIGN.md
---

# nl2sql weekly load (ta-load-weekly) — in-process default

- Registry client `nl2sql` → `repo_id=nl2sql` (`yoosungung/nl2sql`); sync ephemeral path, do not use `/workspace/repo`.
- `.factory/quality.yaml` `load.command`: `cd backend && uv run python ../load/smoke.py`
- Weekly default is **in-process** ASGI + FakeAgent when `LOAD_BASE_URL` unset (no SGLang). Live needs `LOAD_BASE_URL` + `LOAD_REAL_LLM=1`.
- Manual NF #681 (2026-08-13): sha `7f519f2` → OK chat=20/20 errors=0 p95_ms≈113 wall_s≈0.19.
