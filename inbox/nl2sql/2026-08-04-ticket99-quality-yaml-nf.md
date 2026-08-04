---
id: inbox-nl2sql-ticket99-quality-yaml-nf
agent: nl2sql
ticket_id: 99
updated: 2026-08-04
status: inbox
sources:
  - ticket:99
  - .factory/quality.yaml
  - https://github.com/yoosungung/sw-factory/blob/main/examples/tenant-quality/README.md
  - spider2-eval/DESIGN.md
---

# nl2sql quality.yaml NF sections (#99)

- Registered real weekly commands: `opik` (`spider2-opik check`), `clean_code` (backend ruff), `load` (`load/smoke.py` in-process `/api/health`; optional `LOAD_BASE_URL`).
- Stubs from `examples/tenant-quality/` are schema-only; do not copy echo stubs.
- Opik needs repo `.env` (`OPIK_*`, Postgres URL, Spider2 paths) — see spider2-eval/DESIGN.md §4.
