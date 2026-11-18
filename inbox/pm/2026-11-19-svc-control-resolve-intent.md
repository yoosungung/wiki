---
id: inbox-pm-svc-control-resolve-intent
agent: pm
ticket_id: 51bc0936-b896-4919-b94e-d1f0ee94e3e3
updated: 2026-11-19
status: inbox
sources:
  - ticket:51bc0936-b896-4919-b94e-d1f0ee94e3e3
  - https://github.com/yoosungung/aura/pull/32
---

# aura M3 — svc-control 최소 resolve Intent pass

- Fixed: `source_meta`/`user_meta` DDL+FORCE RLS, resolve wire `control.resolve.done`, 1-depth cfg merge (user wins), `secrets_ref` only.
- Deferred: NATS `aura.rpc.control.resolve` bridge Deployment, HTTP admin.
- Gate: `check-svc-control-resolve.sh` + `resolve.selftest.js`.
- PR #32 MERGED; ticket done.
