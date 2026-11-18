---
id: inbox-aura-gateway-run-id-sse-ws
agent: aura
ticket_id: c2b44645-3a15-4e5c-a37a-b4882e3a9668
updated: 2026-11-19
status: inbox
sources:
  - ticket:c2b44645-3a15-4e5c-a37a-b4882e3a9668
  - ARCHITECTURE.md §3.5
  - deploy/docs/gateway-sse-ws.md
---

# Aura Gateway run_id · SSE/WS · principal

- Gateway가 `run_id`를 **UUIDv7**로 발급하고 `aura.tasks.agent.invoke`에 publish한다(클라이언트 미발급).
- 스트림 구독은 **exact** `aura.stream.<run_id>`만 — `*`/`>` 와일드카드 금지.
- SSE/WS는 `run_id` 소유 `principal.id`+`tenant_id`만 허용(불일치 403, 미등록 404).
- Gateway Deployment는 **replicas≥2**, Fission MQT/scale-to-zero/PG 없음. Fair Queue·live NATS는 후속.
- 정적 게이트: `bash deploy/scripts/check-gateway-sse-ws.sh`.
