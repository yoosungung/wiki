---
id: inbox-aa-unitutor-lti-jwks-unsigned-fail
agent: aa
ticket_id: 4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
updated: 2026-10-04
status: inbox
sources:
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# UniTutor LTI launch: unsigned JWT default = security fail

- UniTutor repo has no `.factory/quality.yaml` → mechanical `security.command` skipped; AA tip↔merge skim applies.
- Production default `verifyIdToken` falls back to `decodeIdTokenPayloadUnsafe` (payload decode, no Platform JWKS signature). DESIGN admits “실 JWKS는 후속”.
- Attack sketch: start `/lti/oidc/login` with seeded deployment → capture `state`/`nonce` → forge unsigned `id_token` matching claims → `POST /lti/launch` upserts arbitrary `sub` learner and 302 to FE with `ltiLearnerId`.
- Gate: `aa: security fail` until Workers default verifies JWT against deployment `jwks_url` (and reject unsigned).
- Secondary (non-blocker alone): `target_link_uri` not allowlisted; FE query `ltiLearnerId` is not a server session — keep client-local until signed session cookie or equivalent.
