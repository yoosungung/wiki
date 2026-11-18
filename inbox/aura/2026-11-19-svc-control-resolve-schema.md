---
id: inbox-aura-svc-control-resolve-schema
agent: aura
ticket_id: 51bc0936-b896-4919-b94e-d1f0ee94e3e3
updated: 2026-11-19
status: inbox
sources:
  - ticket:51bc0936-b896-4919-b94e-d1f0ee94e3e3
  - https://github.com/yoosungung/aura
---

# svc-control 최소 resolve 스키마 (Aura M3)

- 테이블명 고정: `source_meta` / `user_meta` (+ tenant RLS, `secrets_ref` only).
- Resolve wire: `aura.rpc.control.resolve` → `control.resolve.done` with 1-depth cfg merge (user wins).
- NATS bridge Deployment·HTTP admin은 별 M3 항목 — 스키마 슬라이스와 분리.
- 게이트: `deploy/scripts/check-svc-control-resolve.sh` + `services/control/resolve.selftest.js`.
