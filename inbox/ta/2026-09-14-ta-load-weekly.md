---
id: inbox-ta-2026-09-14-ta-load-weekly
agent: ta
ticket_id: null
updated: 2026-09-14
status: inbox
sources:
  - schedule:ta-load-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md
---

# ta-load-weekly 2026-09-14

## Sync

- synced: repo_id=sw-factory sha=20f8190 path=/tmp/tenant-repos/sw-factory
- synced: repo_id=nl2sql sha=401b55b path=/tmp/tenant-repos/nl2sql
- synced: repo_id=candidate sha=46379de path=/tmp/tenant-repos/candidate
- synced: repo_id=codingland sha=03e1714 path=/tmp/tenant-repos/codingland

## Load (test / weekly in-process)

| client | project_id | result | evidence |
| --- | --- | --- | --- |
| sw-factory | 5 | skip | no `.factory/quality.yaml` |
| nl2sql | 6 | pass | `cd backend && uv run python ../load/smoke.py` → `OK: load smoke in-process … chat=20/20 errors=0 p95_ms=140.6` (log `/tmp/ta-load-weekly/nl2sql-load-20260914T020115.log`) |
| candidate | 7 | skip | no `.factory/quality.yaml` |
| codingland | 8 | skip | quality.yaml present but no `load.command` (extension Non-goal) |

## NF tickets

- NF=0 (failures only; skip ≠ fail). Feature tickets not touched.
- long_run: nl2sql `load` has no `long_run: true`; completed foreground (~4s) — detach/nf-progress N/A this run.
