---
id: inbox-ta-2026-08-31-ta-load-weekly
agent: ta
ticket_id: null
updated: 2026-08-31
status: inbox
sources:
  - schedule:ta-load-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md
---

# ta-load-weekly 2026-08-31

## Sync
- synced: repo_id=sw-factory sha=87c623a path=/tmp/tenant-repos/sw-factory
- synced: repo_id=nl2sql sha=fe3fe22 path=/tmp/tenant-repos/nl2sql
- synced: repo_id=candidate sha=e965668 path=/tmp/tenant-repos/candidate
- synced: repo_id=codingland sha=52a28b9 path=/tmp/tenant-repos/codingland

## Load
- sw-factory: skip — no `.factory/quality.yaml` (NF 미생성)
- nl2sql: ran in-process (`cd backend && uv run python ../load/smoke.py`) — OK chat=20/20 errors=0 p95_ms=139.9; unit `load/test_smoke.py` 3 passed; log `/tmp/load-weekly-logs/nl2sql-load-20260831-020102.log`
- candidate: skip — no `.factory/quality.yaml`
- codingland: skip — quality.yaml에 `load.command` 없음 (extension Non-goal)

## NF tickets
- NF=0 (실패/회귀 없음). Feature Done 변경 없음.
