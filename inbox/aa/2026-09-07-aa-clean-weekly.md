---
id: inbox-aa-2026-09-07-aa-clean-weekly
agent: aa
ticket_id: null
updated: 2026-09-07
status: inbox
sources:
  - schedule:aa-clean-weekly
  - /tmp/tenant-repos/nl2sql/.factory/quality.yaml
  - /tmp/tenant-repos/codingland/.factory/quality.yaml
---

# aa-clean-weekly 2026-09-07

## Sync

- synced: repo_id=sw-factory sha=87c623a path=/tmp/tenant-repos/sw-factory
- synced: repo_id=nl2sql sha=a698a18 path=/tmp/tenant-repos/nl2sql
- synced: repo_id=candidate sha=bcfcc20 path=/tmp/tenant-repos/candidate
- synced: repo_id=codingland sha=baa050e path=/tmp/tenant-repos/codingland

## Mechanical

- sw-factory / candidate: skip — no `.factory/quality.yaml` `clean_code:` block
- nl2sql: `cd backend && uv sync --extra dev --locked && uv run ruff check . && uv run mypy src && uv run pytest` → exit 0 (343 passed); not long_run
- codingland: `npm --prefix extension run ci` → exit 1 — jest 90 passed; `test:vscode` spawnSync xvfb-run ENOENT (detached + /tmp/nf-progress)

## Heuristic → tickets

- nl2sql: High #1747 err.swallowed `_source_exists_in_repo`; Med #1748 struct.scatter metadata router. Prior Done smells (list head_error, tool_result ok, _run_3step_op) look remediated.
- codingland: Med #1749 test.coupled xvfb; #1750 obj.god CanvasSession; #1751 design.fragility delta vs MAX_CANVAS_NODES. Prior #1505/#1506 largely remediated (provider thin + ingest unit test).
