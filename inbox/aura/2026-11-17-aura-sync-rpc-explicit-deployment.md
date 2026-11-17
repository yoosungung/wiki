---
id: inbox-aura-sync-rpc-explicit-deployment
agent: aura
ticket_id: 817796ca-a69e-4507-8480-b320b76cb34a
updated: 2026-11-17
status: inbox
sources:
  - ticket:817796ca-a69e-4507-8480-b320b76cb34a
  - https://github.com/yoosungung/aura/pull/7
---

# Aura sync Core RR = 명시 Deployment (Fission node-env 아님)

- Stock Fission `node-env`는 specialize 전/후에도 NATS Core에 자동 subscribe하지 않는다. `aura.rpc.*` Warm 응답자는 ARCHITECTURE §4.3 **동일 이미지 명시 Deployment**가 안전하다.
- M0 샘플: Deployment `aura-rpc-smoke-rr` · `nats reply -q aura-rpc-smoke` · subject `aura.rpc.smoke` · replicas≥2 · **JetStream MQT/lag 미연결**.
- Fission Function `aura-rpc-smoke`(`newdeploy` MinScale≥2)는 V0.1 분리 Warm Pool 불변용으로 유지; Core RR 구독 본체는 Deployment.
- 검증: `smoke-sync-rpc.sh` — Warm RR · replicas=0 → No Responders · 1파드 삭제 후 queue HA · 단일 홉 p95≪1s.
