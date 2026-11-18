---
id: inbox-aura-cnpg-pooler-decision
agent: aura
ticket_id: 2a04d47b-6e53-4df2-a8bb-c3d63924828d
updated: 2026-11-18
status: inbox
sources:
  - ticket:2a04d47b-6e53-4df2-a8bb-c3d63924828d
  - ticket:88a7518f-575a-4985-a580-dff0c6be89b4
  - https://github.com/yoosungung/aura/pull/11
---

# Aura M1 Pooler = CloudNativePG Pooler

- 제품: CloudNativePG `Pooler`, `spec.pgbouncer.poolMode: transaction`
- 앱 DSN 호스트 = pooler Service DNS only (PG Pod IP / primary Service 금지)
- standalone PgBouncer = CNPG 미도입 폴백만
- 클러스터 설치·V1.1 RLS 스모크는 child `92cccf21` 후속
