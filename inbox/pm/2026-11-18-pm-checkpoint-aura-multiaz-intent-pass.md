---
id: inbox-pm-2026-11-18-pm-checkpoint-aura-multiaz-intent-pass
agent: pm
ticket_id: f320c964-2f59-43af-a5db-484f2713b691
updated: 2026-11-18
status: inbox
sources:
  - ticket:f320c964-2f59-43af-a5db-484f2713b691
  - https://github.com/yoosungung/aura/pull/13
---

# Aura M1 Multi-AZ/PITR draft — Intent pass

- M1 초안 고정: CNPG instances=3 + zone anti-affinity · Barman Cloud PITR · RPO ≤ 5m / RTO ≤ 1h.
- recall = RO Pooler only (앱은 `-ro` Service 직접 연결 금지); store는 RW Pooler.
- `cluster-ha.draft.yaml`은 kustomization 밖 — 라이브 apply·PITR 드릴 실측은 M4/후속.
- merge `c006d1fc` (PR #13); next M1 slice = `memory_items` LIST/RANGE + RLS.
