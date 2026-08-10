---
id: inbox-ta-ta-load-weekly-2026-08-10
agent: ta
ticket_id: null
updated: 2026-08-10
status: inbox
sources:
  - schedule:ta-load-weekly
  - clients-repos-registry.json
  - /tmp/tenant-repos/nl2sql/.factory/quality.yaml
---

# ta-load-weekly 2026-08-10

## Sync evidence
- synced: repo_id=sw-factory sha=60bac74 path=/tmp/tenant-repos/sw-factory
- synced: repo_id=nl2sql sha=37f8938 path=/tmp/tenant-repos/nl2sql
- synced: repo_id=candidate sha=984be1f path=/tmp/tenant-repos/candidate
- synced: repo_id=codingland sha=aad820e path=/tmp/tenant-repos/codingland

## Load results
- sw-factory (project_id=5): skip — no `.factory/quality.yaml` `load:` (factory repo; example only under `examples/tenant-quality/`)
- nl2sql (project_id=6): OK — `cd backend && uv run python ../load/smoke.py` in-process; chat=20/20 errors=0 p95_ms=139.3 wall_s=0.21 (not `long_run`; no detach)
- candidate (project_id=7): skip — no `.factory/quality.yaml`
- codingland (project_id=8): skip — no `.factory/quality.yaml`

## Tickets
- No New NF tickets (no load failures). Feature Done gates untouched.
