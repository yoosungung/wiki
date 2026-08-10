---
id: inbox-qa-2026-08-10-qa-bulk-weekly
agent: qa
ticket_id: 428
updated: 2026-08-10
status: inbox
sources:
  - ticket:428
  - wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026.md
  - /tmp/tenant-repos/nl2sql/.factory/quality.yaml
---

# qa-bulk-weekly 2026-08-10

- Registry clients synced: sw-factory e3ff0e7, nl2sql 0bf2886, candidate 984be1f, codingland aad820e under `/tmp/tenant-repos/<repo_id>`.
- Only **nl2sql** has `.factory/quality.yaml` with `opik:` (`long_run: true`); no client has `bulk_api:`.
- sw-factory / candidate / codingland: skip bulk/Opik — missing `.factory/quality.yaml` (factory has `examples/tenant-quality` only).
- nl2sql weekly: check pass · gold-sql pass_rate=1.0 · **agent smoke fail pass_rate=0.0** (experiment `weekly-agent-smoke`) → New ticket #428.
- Gap: `spider2-opik run` always exits 0; weekly hard gate does not yet fail on pass_rate=0 despite quality.yaml/#391 wording.
