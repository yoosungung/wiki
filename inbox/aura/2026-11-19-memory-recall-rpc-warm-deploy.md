---
id: inbox-aura-memory-recall-rpc-warm-deploy
agent: aura
ticket_id: 25b46548-311f-438b-ad34-a408eeab56ea
updated: 2026-11-19
status: inbox
sources:
  - ticket:25b46548-311f-438b-ad34-a408eeab56ea
  - https://github.com/yoosungung/aura/pull/27
---

# Aura M2: recall RPC Warm Pool deploy (no MQT)

- `aura.rpc.memory.recall` = sync Core RR: Function `newdeploy` MinScale≥2 + Deployment `aura-memory-recall-rr` replicas≥2, queue-group `aura-memory-recall`.
- **No** MessageQueueTrigger / JetStream lag ScaledObject (RPC scale-to-zero 금지 — No Responders).
- Stub handler returns `memory.recall.done` / empty `items`; hybrid RRF + `SET LOCAL iterative_scan` SELECT = sibling ticket.
- Gate: `bash deploy/scripts/check-memory-recall.sh` (no cluster).
