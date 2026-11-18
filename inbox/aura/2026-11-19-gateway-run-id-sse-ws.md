---
id: inbox-aura-gateway-run-id-sse-ws
agent: aura
ticket_id: c2b44645-3a15-4e5c-a37a-b4882e3a9668
updated: 2026-11-19
status: inbox
sources:
  - ticket:c2b44645-3a15-4e5c-a37a-b4882e3a9668
  - ticket:6a457aa6-1c75-4e0f-ace3-f6cb01baa104
---

# Gateway run_id + SSE/WS + principal

- UUIDv7 `run_id` 발급 후 `aura.tasks.agent.invoke` publish; response 202 + `stream_subject`.
- SSE/WS bridge: exact `aura.stream.<run_id>` only (wildcard 금지); owner principal 403/404.
- Deployment replicas≥2 · MQT/PG 없음. Fair Queue/live NATS = 후속.
- Gate: `bash deploy/scripts/check-gateway-sse-ws.sh`.
