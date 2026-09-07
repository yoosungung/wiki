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

- tenant-repo-sync 4/4: sw-factory `87c623a`, nl2sql `3b70ad7`, candidate `bcfcc20`, codingland `03e1714` (branch=`master` — remote HEAD; `main` ref 없음).
- bulk_api: 전 클라이언트 skip (키 없음 또는 quality.yaml 부재). NF 미생성.
- opik: nl2sql만 실행 (`long_run:true` detach). check→gold-sql→agent hard 전부 exit=0, pass_rate=1.0 (local008,local022). 실험명 `weekly-gold-sql-smoke` / `weekly-agent-smoke`.
- codingland/sw-factory/candidate: opik·bulk_api skip (사유 기록). NF=0.
- long-run: ARCHITECTURE §2.6 #10 — pid log `/tmp/qa-bulk-weekly-nl2sql-opik.log` + `nf-progress.json` phase=done; tracking #1753 Done.
