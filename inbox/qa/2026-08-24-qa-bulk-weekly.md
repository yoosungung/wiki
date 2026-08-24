---
id: inbox-qa-2026-08-24-qa-bulk-weekly
agent: qa
ticket_id: 1206
updated: 2026-08-24
status: inbox
sources:
  - ticket:1206
  - schedule:qa-bulk-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
---

# qa-bulk-weekly 2026-08-24

- Sync evidence: sw-factory `6677716`, nl2sql `c07d9c1`, candidate `364b125`, codingland `f4ea6cc` under `/tmp/tenant-repos/<repo_id>`.
- Gate skip (no NF): sw-factory/candidate — no `.factory/quality.yaml`; codingland — `e2e` only (no `bulk_api`/`opik`).
- nl2sql `opik.command` weekly: check + gold-sql + agent smoke all exit 0; pass_rate 1.0 on local008,local022; tracking #1206 Done.
- Ephemeral checkout needs `SPIDER2_TMP_DIR` or symlink to populated `.tmp-spider2` before `spider2-opik weekly` (depth-1 clone omits gitignored assets).
