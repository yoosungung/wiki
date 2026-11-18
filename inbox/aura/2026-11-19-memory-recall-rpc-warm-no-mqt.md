---
id: inbox-aura-memory-recall-rpc-warm-no-mqt
agent: aura
ticket_id: 25b46548-311f-438b-ad34-a408eeab56ea
updated: 2026-11-19
status: inbox
sources:
  - ticket:25b46548-311f-438b-ad34-a408eeab56ea
  - ticket:1d669034-018b-45e0-986f-c50b24cfd735
  - https://github.com/yoosungung/aura/pull/27
---

# Aura M2 recall RPC Warm Pool (no MQT)

- `aura.rpc.memory.recall` = Core RR only: Deployment `aura-memory-recall-rr` replicas≥2 + queue-group `aura-memory-recall`; Function `newdeploy` MinScale≥2.
- Recall 경로에 MessageQueueTrigger / JetStream lag ScaledObject **금지** (async store/embed와 분리 배포).
- 본 슬라이스는 deploy stub (`mode:stub`, `items:[]`); hybrid RRF · iterative_scan SQL은 sibling.
- 정적 게이트: `bash deploy/scripts/check-memory-recall.sh`.
