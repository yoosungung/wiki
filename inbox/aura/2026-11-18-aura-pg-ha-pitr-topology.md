---
id: inbox-aura-pg-ha-pitr-topology
agent: aura
ticket_id: f320c964-2f59-43af-a5db-484f2713b691
updated: 2026-11-18
status: inbox
sources:
  - ticket:f320c964-2f59-43af-a5db-484f2713b691
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - https://github.com/yoosungung/aura/pull/13
  - https://cloudnative-pg.io/documentation/1.24/recovery/
---

# Aura M1 — PG Multi-AZ / PITR 토폴로지 초안

- CNPG `instances≥3` + zone anti-affinity; Barman object-store PITR (destination TBD/M2)
- **RPO ≤ 5m · RTO ≤ 1h** (M1 초안; 드릴 실측 M4)
- recall = 옵트인 RO Pooler (`type: ro`); store = RW Pooler only
- 본문: aura `deploy/docs/pg-ha-pitr-topology.md` · gate `check-pg-ha.sh`
