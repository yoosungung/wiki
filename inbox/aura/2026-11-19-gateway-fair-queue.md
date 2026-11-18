---
id: inbox-aura-2026-11-19-gateway-fair-queue
agent: aura
ticket_id: 605ca218-b321-437f-99b6-429b2f13dc67
updated: 2026-11-19
status: inbox
sources:
  - ticket:605ca218-b321-437f-99b6-429b2f13dc67
  - https://github.com/yoosungung/aura/pull/35
---

# Gateway Fair Queue (CAS KV)

- `services/gateway/rate-limit.js`: `createTenantRateLimiter` + `createMemoryKv` CAS (`get`/`cas`); 키 `quota.{tenant_id}`; 기본 `ratePerSec` 10 · burst 30 · `maxInflight` 20.
- `gateway.js`: `tryAcquire` before `aura.tasks.agent.invoke` publish; `release` on publish failure 및 stream terminal frame.
- 노이지 픽스처: 동일 KV에서 tenant A 429여도 tenant B는 202 (`gateway.selftest.js`).
- 검증: `node services/gateway/gateway.selftest.js`, `bash deploy/scripts/check-gateway-fair-queue.sh`, `bash deploy/scripts/check-gateway-sse-ws.sh`.