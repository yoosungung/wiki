---
id: inbox-nl2sql-metadata-inspect-extract
agent: nl2sql
ticket_id: 1748
updated: 2026-09-07
status: inbox
sources:
  - ticket:1748
  - wiki/Engineering/AI-Native-Engineering/Smell-Agglomeration-Module-Split.md
---

# metadata inspect module extract

- Warehouse inspect (`_source_exists_in_repo` + `inspect_source`) lives in `routers/metadata_inspect.py`; fs/write stay in `metadata.py`.
- Register both routers under `/api` in `app.py` — HTTP path unchanged.
- Corrupt-source warning logger name is `nl2sql_backend.routers.metadata_inspect` after the move.
