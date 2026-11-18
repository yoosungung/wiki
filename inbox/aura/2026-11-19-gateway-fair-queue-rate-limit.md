---
id: inbox-aura-gateway-fair-queue-rate-limit
agent: aura
ticket_id: 605ca218-b321-437f-99b6-429b2f13dc67
updated: 2026-11-19
status: inbox
sources:
  - ticket:605ca218-b321-437f-99b6-429b2f13dc67
  - https://github.com/yoosungung/aura/pull/35
---

# Aura Gateway Fair Queue / Rate Limit (M3)

- Gateway submit는 `acquireForRun`으로 테넌트별 Token Bucket + max_inflight 검사 후에만 `aura.tasks.agent.invoke` publish (기본 10/s · burst 30 · inflight 20).
- 상태 키 `quota:{tenant_id}` — memory `createMemoryQuotaStore` 테스트; 생산은 NATS JetStream KV 권장(live 클라이언트는 후속).
- 거부 시 429 (`rate_limited` | `max_inflight_exceeded`) + `retry_after_ms`; JetStream 미적재.
- V3.2: A 폭주해도 B는 202 — `gateway.selftest.js` 노이지 픽스처 · `check-gateway-fair-queue.sh`.
- `releaseInflight(tenant, run_id)` API 제공; done/error 구독 배선·우회 재확인은 별 ROADMAP 항목.
