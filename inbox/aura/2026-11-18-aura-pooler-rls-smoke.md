---
id: inbox-aura-pooler-rls-smoke
agent: aura
ticket_id: 92cccf21-e2e4-48c7-b9cd-a495f1fb9d15
updated: 2026-11-18
status: inbox
sources:
  - ticket:92cccf21-e2e4-48c7-b9cd-a495f1fb9d15
  - https://github.com/yoosungung/aura/pull/12
---

# Aura V1.1 Pooler + RLS smoke

- 픽스처 `deploy/k8s/pg-pooler/rls-smoke-fixture.sql`: `FORCE ROW LEVEL SECURITY` + `app.tenant_id` GUC 정책.
- `smoke-pg-pooler.sh`: (a) DSN=pooler only (b) poolMode=transaction (c) A→COMMIT→B 미노출 (d) session `set_config(..., false)` 정적 금지.
- 라이브는 pooler Service DSN으로만; `SMOKE_PG_POOLER_STATIC=1`은 클러스터 없이 게이트.
- PgBouncer transaction 모드에서 픽스처 DDL은 `BEGIN`/`COMMIT`으로 감싸 백엔드 레이스 완화.
