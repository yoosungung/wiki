---
id: inbox-aura-inflight-release-bypass
agent: aura
ticket_id: 5f299c68-2d2d-458f-a055-86cbe2ec91b9
updated: 2026-11-19
status: inbox
sources:
  - ticket:5f299c68-2d2d-458f-a055-86cbe2ec91b9
  - https://github.com/yoosungung/aura/pull/36
---

# Gateway inflight release + agent_invoke bypass re-check (M3 §2.2)

- Terminal: stream `run.completed`/`error` · events `aura.events.agent.invoke.done`/`error` → `rateLimiter.release` (멱등).
- 우회 publish 방어: `agent_invoke` `ensureAdmitted(tenant_id, run_id)`; 초과 → HTTP 429 `agent.invoke.error` + `poison` (턴/RPC 없음).
- Gateway 경유 run_id는 `runs` 멱등 통과; live NATS done 구독 Deployment는 후속.
- 검증: `check-gateway-inflight-release.sh` · `gateway.selftest` · `handler.selftest`.