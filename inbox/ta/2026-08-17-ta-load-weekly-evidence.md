---
id: inbox-ta-2026-08-17-ta-load-weekly-evidence
agent: ta
ticket_id: null
updated: 2026-08-17
status: inbox
sources:
  - schedule:ta-load-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md
---

# ta-load-weekly 2026-08-17

## Sync
- synced: repo_id=sw-factory sha=63f611c path=/tmp/tenant-repos/sw-factory
- synced: repo_id=nl2sql sha=ba6d00e path=/tmp/tenant-repos/nl2sql
- synced: repo_id=candidate sha=7bf9b29 path=/tmp/tenant-repos/candidate
- synced: repo_id=codingland sha=f4ea6cc path=/tmp/tenant-repos/codingland

## Load
- sw-factory: skip — no `.factory/quality.yaml` (NF 없음)
- nl2sql: ran `cd backend && uv run python ../load/smoke.py` (in-process, LOAD_BASE_URL unset) → OK chat=20/20 errors=0 p95_ms=135.0 wall_s=0.17; log=/tmp/ta-load-weekly-nl2sql-20260817T020102Z.log; long_run=false (opik only)
- candidate: skip — no `.factory/quality.yaml`
- codingland: skip — quality.yaml에 `load:` 키 없음

## NF
- New tickets: 0 (실패 없음). feature Done 게이트 미변경.
