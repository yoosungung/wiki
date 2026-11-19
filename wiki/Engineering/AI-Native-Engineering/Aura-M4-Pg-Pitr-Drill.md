---
id: aura-m4-pg-pitr-drill
title: "Aura M4: PG PITR drill #1 (lab RPO/RTO)"
status: canonical
owner: km
updated: "2026-11-20"
last_updated: "2026-11-20"
review_after: "2027-02-20"
sources:
  - inbox/aura/2026-11-19-aura-pg-pitr-drill.md
  - ticket:996b3f7e-82d9-48a4-8196-b8e949fe401d
  - https://github.com/yoosungung/aura/pull/57
  - https://cloudnative-pg.io/documentation/1.23/recovery/
tags: ["Engineering", "Aura", "Postgres", "PITR", "CNPG"]
type: wiki
---

# Aura M4: PG PITR drill #1 (lab RPO/RTO)

- Lab Docker Postgres 16 + WAL `archive_command` stand-in for CNPG Barman; measured **RPO≈3.2s · RTO≈3.1s** → budgets **≤5m / ≤1h confirmed** (do not shrink budgets from lab scale).
- Trap: `recovery_target_time` must be **after commit** — row `created_at` (statement start) can stop recovery *before* the desired commit; use post-commit `clock_timestamp()`.
- Trap: bind-mounted archive files need world-readable mode for container UID 70; restore PGDATA must be chown'd to postgres UID.
- Restore is always a **new** Cluster (`bootstrap.recovery` + `targetTime`); never in-place overwrite. App cutover = Pooler DSN only.
- Gates: `check-pg-pitr-drill.sh` + committed `services/ops/pitr-drill/drill-1.record.json`; CNPG/Barman scale re-drill = M5.
