---
id: inbox-qa-2026-08-17-qa-bulk-weekly-evidence
agent: qa
ticket_id: 924
updated: 2026-08-17
status: inbox
sources:
  - schedule:qa-bulk-weekly
  - ticket:924
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# qa-bulk-weekly 2026-08-17 evidence

## Sync
- synced: repo_id=sw-factory sha=63f611c path=/tmp/tenant-repos/sw-factory
- synced: repo_id=nl2sql sha=85cba02 path=/tmp/tenant-repos/nl2sql
- synced: repo_id=candidate sha=7bf9b29 path=/tmp/tenant-repos/candidate
- synced: repo_id=codingland sha=f4ea6cc path=/tmp/tenant-repos/codingland

## Gates
- sw-factory: skip bulk_api+opik reason=no `.factory/quality.yaml`
- candidate: skip bulk_api+opik reason=no `.factory/quality.yaml`
- codingland: skip bulk_api+opik reason=quality.yaml has e2e only (no bulk_api/opik keys)
- nl2sql: skip bulk_api reason=no `bulk_api:` key; ran `opik.command` (long_run detach)

## nl2sql opik weekly
- command: `cd spider2-eval && uv run spider2-opik weekly`
- SPIDER2_TMP_DIR: ephemeral checkout symlink → workspace `.tmp-spider2` (gitignored assets)
- check OK → gold-sql weekly-gold-sql-smoke pass_rate=1.0 → agent weekly-agent-smoke pass_rate=1.0
- EXIT:0; NF New tickets for failures: 0
- tracking ticket #924 for nf-progress; log=/tmp/qa-bulk-weekly-nl2sql-opik-20260817T0302Z.log

## Pitfall
- Fresh tenant-repo-sync clone lacks `.tmp-spider2/Spider2` — set/link SPIDER2_TMP_DIR to existing assets or fail check hard.
