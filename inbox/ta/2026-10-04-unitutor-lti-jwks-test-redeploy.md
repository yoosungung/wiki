---
id: inbox-ta-unitutor-lti-jwks-test-redeploy
agent: ta
ticket_id: 4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
updated: 2026-10-04
status: inbox
sources:
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - https://github.com/yoosungung/UniTutorAI/pull/29
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37168058116
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
---

# UniTutor LTI JWKS tip test redeploy smoke

- tip `138eab1` (PR #29) push Deploy run 37168058116 success — Cloudflare Workers+Pages single env (no k8s / no `.factory/cd.yaml`).
- Live JWKS fail-closed: temporary D1 `lti_deployments` smoke row → OIDC login 302 → `POST /lti/launch` with `alg=none` unsigned JWT + valid state → **401 `invalid_token`**; seed deleted after probe.
- Smoke hosts: `api.tutor.askwho.net/health` 200 · `unitutor.askwho.net` 200 · unknown_deployment 404 after cleanup.
