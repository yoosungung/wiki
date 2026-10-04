---
id: unitutor-lti-13-b2b
title: "UniTutor LTI 1.3 B2B: Option B + JWKS fail-closed"
status: canonical
owner: km
updated: "2026-10-05"
review_after: "2027-01-05"
sources:
  - inbox/uni-tutor/2026-10-04-lti-b2b-proposal.md
  - inbox/uni-tutor/2026-10-04-lti-option-b-spike.md
  - inbox/uni-tutor/2026-10-04-lti-jwks-verify.md
  - inbox/uni-tutor/2026-10-04-lti-jwks-verify-default.md
  - inbox/aa/2026-10-04-unitutor-lti-jwks-unsigned-fail.md
  - inbox/aa/2026-10-04-unitutor-lti-jwks-remount-review.md
  - inbox/aa/2026-10-04-unitutor-lti-jwks-security-pass.md
  - inbox/qa/2026-10-04-unitutor-lti-jwks-qa-pass.md
  - inbox/ta/2026-10-04-unitutor-d1-lti-test-deploy.md
  - inbox/ta/2026-10-04-unitutor-lti-jwks-test-redeploy.md
  - inbox/pm/2026-10-04-unitutor-lti-option-b-intent-pass.md
  - inbox/pm/2026-10-04-unitutor-lti-jwks-intent-pass.md
  - inbox/pm/2026-10-04-unitutor-lti-b2b-done.md
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - https://github.com/yoosungung/UniTutorAI/pull/24
  - https://github.com/yoosungung/UniTutorAI/pull/28
  - https://github.com/yoosungung/UniTutorAI/pull/29
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
tags: ["Engineering", "AI-Native", "UniTutor", "LTI", "Security"]
type: "wiki"
---

# UniTutor LTI 1.3 B2B: Option B + JWKS fail-closed

## Scope

- LTI **1.3** Resource Link launch only (OIDC login → `id_token` POST → canvas). LTI 1.1 / AGS / NRPS / Deep Linking excluded.
- Eric-approved **Option B**: D1 learner key `(iss, client_id, deployment_id, sub)`.
- Public API: `GET /lti/oidc/login`, `POST /lti/launch` → FE `?courseId=&ltiLearnerId=`. Existing `POST /api/tutor/turn` unchanged.

## Security SoR

- Workers **default** is `verifyIdTokenWithJwks` (`jose` + deployment `jwks_url`, RS256, exp/iat ±60s). Unsigned / `alg=none` rejected.
- `decodeIdTokenPayloadUnsafe` is **test-only**. Prior tip without JWKS default → `aa: security fail`.
- FE: `lib/ltiLaunch.ts` persists `ltiLearnerId`, strips URL params. Query `ltiLearnerId` is not a server session.
- Residual NF: allowlist `target_link_uri` / redirect_uri; pilot LMS seed for happy-path smoke.

## Deploy notes

- Real D1 required — placeholder UUID fails CF 10181. Create `unitutor` D1 → bind in `backend/wrangler.jsonc`; migrations apply **before** Worker deploy.
- CD = Cloudflare single env (`deploy.yml`), not k8s `tenant_cd`.
- Evidence tip `138eab1` (PR #29): Deploy 37168058116; live `alg=none` → 401 `invalid_token` (temp D1 seed then deleted).

## Related

- [[wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/Cloudflare-D1-Migrations-Before-Worker-Deploy.md]]
- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
