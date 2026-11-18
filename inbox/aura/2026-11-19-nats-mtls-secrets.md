---
id: inbox-aura-nats-mtls-secrets
agent: aura
ticket_id: 012df201-9cc9-487c-a450-37dc45cc8a4e
updated: 2026-11-19
status: inbox
sources:
  - ticket:012df201-9cc9-487c-a450-37dc45cc8a4e
  - https://docs.nats.io/reference/config/tls/
---

# Aura M3: NATS mTLS + secrets mask/TTL cache

- §9.2 wire: `deploy/docs/nats-mtls-secrets.md` · overlay `deploy/k8s/nats-mtls/` (`tls { verify: true }`) · Secret keys only (no live PEM in git).
- Control helpers: `maskSecrets` · `createSecretsCache` TTL≤60s · `aura.events.control.secrets.rotated` invalidate · `buildNatsTlsOptions`/`assertNatsMtlsConnect`.
- Gate: `check-nats-mtls-secrets.sh` (offline; live cert CI Non-goal).
- base `nats.yaml` plaintext smoke kept; production apply uses overlay.
