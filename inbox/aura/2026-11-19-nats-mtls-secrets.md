---
id: inbox-aura-nats-mtls-secrets
agent: aura
ticket_id: 012df201-9cc9-487c-a450-37dc45cc8a4e
updated: 2026-11-19
status: inbox
sources:
  - ticket:012df201-9cc9-487c-a450-37dc45cc8a4e
  - deploy/docs/nats-mtls-secrets.md
  - pr:https://github.com/yoosungung/aura/pull/44
---

# Aura M3: NATS mTLS + 시크릿 mask/TTL 캐시

- §9.2: `deploy/k8s/nats-mtls/` — server `tls { verify: true }`, Secret 키만(PEM 값 out-of-band).
- `maskSecrets` / `createSecretsCache` (TTL≤60s) / `handleRotatedEvent` on `aura.events.control.secrets.rotated`.
- 클라이언트: `buildNatsTlsOptions` · `assertNatsMtlsConnect` (`services/control/nats-tls.js`).
- 검증: `bash deploy/scripts/check-nats-mtls-secrets.sh` (live cert 클러스터 불필요).
- PR: https://github.com/yoosungung/aura/pull/44
- Non-goals: F1 · NATS Account · live cert CI 필수 · OTel 전면(M4).