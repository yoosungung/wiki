---
id: inbox-ta-2026-09-07-ta-load-weekly
agent: ta
ticket_id: null
updated: 2026-09-07
status: inbox
sources:
  - schedule:ta-load-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md
---

# ta-load-weekly 2026-09-07

## Sync evidence
- synced: repo_id=sw-factory sha=87c623a path=/tmp/tenant-repos/sw-factory
- synced: repo_id=nl2sql sha=a698a18 path=/tmp/tenant-repos/nl2sql
- synced: repo_id=candidate sha=bcfcc20 path=/tmp/tenant-repos/candidate
- synced: repo_id=codingland sha=baa050e path=/tmp/tenant-repos/codingland

## Load outcomes
- sw-factory: skip — no `.factory/quality.yaml` (NF=0)
- nl2sql: OK in-process health→chat→conversations chat=20/20 errors=0 p95_ms=85.1 wall_s=0.16 (log `/tmp/load-weekly-logs/nl2sql-load-20260907-020100.log`)
- candidate: skip — no `.factory/quality.yaml` (NF=0)
- codingland: skip — quality.yaml present but no `load.command` (extension Non-goal; NF=0)

## Notes
- Feature Done gates untouched. No New NF tickets (pass + mechanical skips only).
- nl2sql `load` is not `long_run`; no detach/nf-progress needed.
