---
id: inbox-aura-cnpg-pooler-transaction-dsn
agent: aura
ticket_id: 88a7518f-575a-4985-a580-dff0c6be89b4
updated: 2026-11-18
status: inbox
sources:
  - ticket:88a7518f-575a-4985-a580-dff0c6be89b4
  - https://github.com/yoosungung/aura/pull/11
---

# Aura M1: CloudNativePG Pooler + pooler-only DSN

- Pooler 제품 확정: **CloudNativePG `Pooler`**, `spec.pgbouncer.poolMode: transaction` (standalone PgBouncer = 폴백만).
- 앱 DSN 호스트: `aura-pg-pooler.aura.svc.cluster.local` only — `aura-pg-rw`/`-r`/`-ro`·Pod IP 금지.
- 설치 경로: `deploy/k8s/pg-pooler` · `install-pg-pooler.sh` (operator chart pin `0.29.2`) · 정적 `check-pg-pooler.sh`.
- V1.1 RLS 재사용 실측은 별 티켓; Multi-AZ는 Cluster `instances` 확장 티켓.
