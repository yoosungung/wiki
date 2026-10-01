---
id: inbox-uni-tutor-cloudflare-deploy-prep
agent: uni-tutor
ticket_id: f7f980f3-ac59-42fc-a462-45ecfe6df2b8
updated: 2026-10-01
status: inbox
sources:
  - ticket:f7f980f3-ac59-42fc-a462-45ecfe6df2b8
  - wiki/Engineering/Infrastructure-and-DevOps/Cloudflare-D1-Migrations-Before-Worker-Deploy.md
---

# UniTutor Cloudflare deploy prep

- Workers `wrangler deploy --config ./wrangler.jsonc` — 상위 monorepo `.wrangler/deploy/config.json`과 동시 find-up 시 redirect 충돌; `--config` 필수.
- D1 미바인딩이면 apply 단계는 N/A. 바인딩 추가 시 wiki대로 apply → deploy를 `npm run deploy`에 고정.
- Pages wrangler v3에는 `pages deploy --dry-run` 없음 → dry-run 스크립트는 `npm run build`.
- FE API origin: 빌드타임 `VITE_API_BASE_URL` → `lib/apiBase.ts` (`apiUrl`).
