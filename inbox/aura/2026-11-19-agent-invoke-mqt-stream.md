---
id: inbox-aura-agent-invoke-mqt-stream
agent: aura
ticket_id: 54a06a7d-631d-424a-8088-3accfe9a74a8
updated: 2026-11-19
status: inbox
sources:
  - ticket:54a06a7d-631d-424a-8088-3accfe9a74a8
  - ticket:6a457aa6-1c75-4e0f-ace3-f6cb01baa104
---

# agent_invoke MQT + aura.stream frames

- MQT: `aura.tasks.agent.invoke` → done/error; consumer `aura_agent_invoke`; `minReplicaCount=0`; PG 금지.
- UX stream: Core `aura.stream.<run_id>` frames `run.started` / `token` / `tool.*` / `run.completed` (JetStream 금지; 정본=events done).
- RPC deps injectable: resolve / recall / mcp.tool; plaintext `secrets` 거부; identifiers-only payload.
- Gate: `bash deploy/scripts/check-agent-invoke.sh` (no cluster).
- Non-goals this slice: Gateway SSE/Fair Queue / live NATS Core publisher / live LLM Gateway.
