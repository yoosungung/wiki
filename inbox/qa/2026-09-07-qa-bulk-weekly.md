---
id: inbox-qa-2026-09-07-qa-bulk-weekly
agent: qa
ticket_id: 1753
updated: 2026-09-07
status: inbox
sources:
  - ticket:1753
  - schedule:qa-bulk-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# qa-bulk-weekly 2026-09-07

- Sync evidence: sw-factory `87c623a`, nl2sql `3b70ad7`, candidate `bcfcc20`, codingland `03e1714` under `/tmp/tenant-repos/<repo_id>`.
- Gate skip: no `bulk_api` on any client; sw-factory/candidate no `.factory/quality.yaml`; codingland has e2e/clean_code only (no opik).
- nl2sql `opik.command` weekly (long_run): detach → check + gold-sql + agent hard all exit 0, pass_rate=1.0 on local008/local022; ticket #1753 Done; NF=0.
- Ephemeral checkout needs `SPIDER2_TMP_DIR` / symlink to populated `.tmp-spider2` (wiki §4.3).
