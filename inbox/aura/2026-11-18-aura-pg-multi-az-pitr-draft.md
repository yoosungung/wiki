---
id: inbox-aura-pg-multi-az-pitr-draft
agent: aura
ticket_id: f320c964-2f59-43af-a5db-484f2713b691
updated: 2026-11-18
status: inbox
sources:
  - ticket:f320c964-2f59-43af-a5db-484f2713b691
  - https://cloudnative-pg.io/documentation/1.23/backup_barmanobjectstore/
  - https://cloudnative-pg.io/documentation/1.23/recovery/
---

# Aura PG Multi-AZ / PITR M1 draft

- CNPG `instances≥3` + zone topology (`affinity.topologyKey` or `topologySpreadConstraints`); smoke stays `instances: 1`.
- PITR = Barman object-store continuous WAL+base; destination TBD (do not invent bucket/region).
- M1 draft SLO: **RPO ≤ 5m**, **RTO ≤ 1h**; drill/measurement = M4.
- recall offload = opt-in CNPG Pooler `type: ro` (`aura-pg-pooler-ro`); apps never hit `-ro` Service directly.
- Gate: `deploy/scripts/check-pg-ha.sh` · doc `deploy/docs/pg-ha-pitr-topology.md` · draft `cluster-ha.draft.yaml`.
