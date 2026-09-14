---
id: inbox-qa-2026-09-14-qa-bulk-weekly
agent: qa
ticket_id: 1985
updated: 2026-09-14
status: inbox
sources:
  - schedule:qa-bulk-weekly
  - ticket:1985
  - ticket:1986
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# qa-bulk-weekly 2026-09-14

## Sync
- synced: repo_id=sw-factory sha=20f8190 path=/tmp/tenant-repos/sw-factory
- synced: repo_id=nl2sql sha=401b55b path=/tmp/tenant-repos/nl2sql
- synced: repo_id=candidate sha=46379de path=/tmp/tenant-repos/candidate
- synced: repo_id=codingland sha=c08dfdd path=/tmp/tenant-repos/codingland

## Suites
| client | project_id | bulk_api | opik |
| --- | --- | --- | --- |
| sw-factory | 5 | skip — no `.factory/quality.yaml` | skip — same |
| nl2sql | 6 | skip — no `bulk_api` key | ran `spider2-opik weekly` (long_run detach) — check/gold exit=0; agent exit=0 hard but pass_rate=0.5 |
| candidate | 7 | skip — no `.factory/quality.yaml` | skip — same |
| codingland | 8 | skip — no `bulk_api`/`opik` keys | skip — same (e2e+clean_code only) |

## Opik (nl2sql)
- gold-sql weekly-gold-sql-smoke pass_rate=1.0 (local008,local022)
- agent weekly-agent-smoke pass_rate=0.5 — local022 match; **local008 baseball result mismatch** (SQL non-empty)
- experiment id `01a09ddd-823c-7283-a288-230665c4e911`; log `/tmp/qa-bulk-weekly-nl2sql-opik-20260914.log`
- `.tmp-spider2` linked from workspace populated tree (tenant-repo-sync depth-1 lacks assets)

## NF
- New #1986 local008 regression (pass_rate 1.0→0.5)
- Tracking #1985 long_run detach

## Trap
- `spider2-opik run` returns exit 0 even when pass_rate&lt;1.0; weekly hard only fails on empty-SQL/pass_rate=0 (or step crash). Smoke regression still needs NF.
