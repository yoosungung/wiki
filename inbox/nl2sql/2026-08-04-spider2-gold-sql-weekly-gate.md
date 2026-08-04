---
id: inbox-nl2sql-spider2-gold-sql-weekly-gate
agent: nl2sql
ticket_id: 121
updated: 2026-08-04
status: inbox
sources:
  - ticket:121
  - ticket:117
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - spider2-eval/DESIGN.md
---

# Spider2 weekly opik.command = check + gold-sql smoke

- `.factory/quality.yaml` `opik.command` is no longer check-only: `spider2-opik check && spider2-opik run --task gold-sql --instance-ids local008,local022`.
- Smoke IDs remain `QUALITY_SMOKE_INSTANCE_IDS` = local008, local022 (wiki §3 / DESIGN §4.1).
- In-cluster env for weekly NF: `OPIK_URL_OVERRIDE=http://opik-frontend.opik.svc.cluster.local:5173/api`, PG `postgresql.postgres.svc.cluster.local`, Spider2 paths per DESIGN §5.
- Verified 2026-08-04: check OK; gold-sql smoke pass_rate **1.0** / spider2_exec_match avg 1.0.
- Agent weekly wiring is out of this ticket (#122/#123); do not fold agent into default opik.command yet.
