---
id: unitutor-cloudflare-deploy
title: "UniTutor Cloudflare 배포 (Pages + Workers + domain)"
status: canonical
owner: km
updated: "2026-10-02"
review_after: "2027-01-02"
sources:
  - inbox/pm/2026-10-01-unitutor-cloudflare-deploy-prep.md
  - inbox/pm/2026-10-01-unitutor-cf-deploy-prep-intent.md
  - inbox/pm/2026-10-01-unitutor-gh-actions-deploy-intent.md
  - inbox/pm/2026-10-01-unitutor-tutor-askwho-domain-intent.md
  - inbox/ta/2026-10-01-unitutor-gh-actions-deploy.yml.md
  - inbox/ta/2026-10-01-unitutor-tutor-askwho-domain.md
  - inbox/uni-tutor/2026-10-01-unitutor-cloudflare-deploy-prep.md
  - https://github.com/yoosungung/UniTutorAI/pull/8
  - https://github.com/yoosungung/UniTutorAI/pull/9
  - https://github.com/yoosungung/UniTutorAI/pull/10
tags: ["Engineering", "DevOps", "Cloudflare", "UniTutor"]
type: "wiki"
---

# UniTutor Cloudflare 배포 (Pages + Workers + domain)

UniTutor 원격 배포는 k8s가 아니라 **Cloudflare**: FE=Pages(`dist/`), BE=Workers(`wrangler`). AGENTS의 k8s 문구와 불일치하면 CF 기준으로 맞춘다.

## 순서

1. (D1 바인딩 있을 때) `d1 migrations apply` → 그다음 deploy. 없으면 apply N/A. 일반 규칙: [[wiki/Engineering/Infrastructure-and-DevOps/Cloudflare-D1-Migrations-Before-Worker-Deploy.md]]
2. Worker `backend` deploy (`wrangler deploy --config ./wrangler.jsonc` — monorepo find-up redirect 회피)
3. Pages `frontend` (`VITE_API_BASE_URL=https://api.tutor.askwho.net`)
4. Smoke: `api.tutor.askwho.net/health` + Pages 루트 `tutor.askwho.net/`

CI: `.github/workflows/deploy.yml` — `main` push + `workflow_dispatch` (sw-factory 패턴). Pages wrangler v3에는 `pages deploy --dry-run` 없음 → dry-run은 `npm run build`.

## Domain

- Pages: `tutor.askwho.net`
- Worker custom_domain: `api.tutor.askwho.net`
- Eric 오타 `tutor.askwhow.net` → 관례상 `askwho.net` zone (factory와 동일)

## 게이트

- Actions secrets: `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`. 없으면 워크플로 파일만 merge, `prod:` 보류.
- macOS에서 `package-lock.json` 재생성 시 `@rollup/rollup-linux-x64-gnu` optional이 빠지면 Linux CI 깨짐 → main lock 기준으로 유지.
