---
id: inbox-ta-unitutor-d1-lti-test-deploy
agent: ta
ticket_id: 4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
updated: 2026-10-04
status: inbox
sources:
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
  - https://github.com/yoosungung/UniTutorAI/pull/28
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
  - wiki/Engineering/Infrastructure-and-DevOps/Cloudflare-D1-Migrations-Before-Worker-Deploy.md
---

# UniTutor D1 unitutor + LTI test deploy

- LTI option B needs real D1; placeholder `00000000-…0001` fails Worker deploy (CF 10181).
- Create `wrangler d1 create unitutor` → uuid `7bc6be4d-4809-4faa-9f38-4a9d7973b6be`; commit into `backend/wrangler.jsonc`.
- `npm run deploy` = `d1 migrations apply DB --remote` then `wrangler deploy` (apply before deploy).
- FRONTEND_ORIGIN prod: `https://unitutor.askwho.net`.
- UniTutor CD remains Cloudflare single env (not k8s tenant_cd).
