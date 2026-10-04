---
id: unitutor-cloudflare-deploy
title: "UniTutor Cloudflare 배포 (Pages + Workers + domain)"
status: canonical
owner: km
updated: "2026-10-05"
review_after: "2027-01-03"
sources:
  - inbox/pm/2026-10-01-unitutor-cloudflare-deploy-prep.md
  - inbox/pm/2026-10-02-unitutor-pages-project-create-ci.md
  - inbox/pm/2026-10-02-unitutor-pages-domain-dns-530.md
  - inbox/pm/2026-10-02-unitutor-pages-domain-dns-gap.md
  - inbox/pm/2026-10-02-unitutor-first-remote-deploy-done.md
  - inbox/ta/2026-10-02-unitutor-pages-wrangler-config.md
  - inbox/ta/2026-10-02-unitutor-pages-custom-domain-api.md
  - inbox/ta/2026-10-02-unitutor-pages-domain-attach-idempotent.md
  - inbox/ta/2026-10-02-unitutor-pages-domain-dns-cname.md
  - inbox/ta/2026-10-02-unitutor-pages-domain-zone-cname.md
  - inbox/ta/2026-10-02-unitutor-dns-list-403-soft-skip.md
  - inbox/ta/2026-10-02-unitutor-pages-dns-list-403-soft-skip.md
  - ticket:25217dd4-521b-452e-ba9f-e4766b3898af
  - https://github.com/yoosungung/UniTutorAI/pull/22
  - inbox/ta/2026-10-04-unitutor-d1-lti-test-deploy.md
  - inbox/ta/2026-10-04-unitutor-lti-jwks-test-redeploy.md
  - ticket:4aa8d43d-4ad6-42b0-bd1c-a0d83caaf061
tags: ["Engineering", "DevOps", "Cloudflare", "UniTutor"]
type: "wiki"
---

# UniTutor Cloudflare 배포 (Pages + Workers + domain)

UniTutor 원격 배포는 k8s가 아니라 **Cloudflare**: FE=Pages(`dist/`), BE=Workers(`wrangler`).

## 순서

1. (D1 있으면) `d1 migrations apply` → deploy. 일반 규칙: [[wiki/Engineering/Infrastructure-and-DevOps/Cloudflare-D1-Migrations-Before-Worker-Deploy.md]]
2. Worker `backend` — `wrangler deploy --config ./wrangler.jsonc` (monorepo find-up 회피)
3. Pages `frontend` — **`wrangler pages deploy`는 `--config` 커스텀 경로 거부**. cwd의 `wrangler.jsonc`만 자동 탐색. Workers와 혼동 금지.
4. Pages project가 없으면 **deploy 전에** project create(CI).
5. Custom domain attach (API) → (가능하면) zone CNAME → Smoke.

CI: `.github/workflows/deploy.yml`. Pages dry-run=`tsc`/`build` (테스트 exclude 필요).

## Domain (운영 SoR, 2026-10-02)

| 역할 | 호스트 | 비고 |
|------|--------|------|
| Pages smoke | `unitutor.askwho.net` | Dashboard DNS; 첫 green Deploy run 37014651191 / PR #22 |
| Worker API | `api.tutor.askwho.net` | health 200 유지 |
| Legacy intent | `tutor.askwho.net` | NXDOMAIN이면 smoke에 쓰지 말 것 (#21 정렬) |

## Attach ≠ public DNS

- Pages Domains API attach **success** alone ≠ public resolve. `dig` empty + edge **530**(1016) 가능.
- Same-account attach가 zone DNS를 항상 만들지 않음. Ensure는 idempotent **proxied CNAME** `host → *.pages.dev` (`deploy/pages_domain_dns.py`)까지.
- Compact JSON grep(`"name":"host"`)는 pretty-print miss → 재POST·400. `pages_domain_attached.py`로 list+already-exists=success.
- Token에 Zone DNS Read/Edit 없으면 `dns_records` **403** → **soft-skip** Ensure, Smoke/Dashboard 신뢰. Hard-fail로 Smoke를 막지 말 것.

## D1 for LTI (2026-10-04)

- LTI Option B needs a **real** D1 binding. Placeholder `00000000-…0001` fails Worker deploy (CF **10181**).
- `wrangler d1 create unitutor` → commit uuid into `backend/wrangler.jsonc` (example uuid `7bc6be4d-4809-4faa-9f38-4a9d7973b6be`).
- `npm run deploy` = `d1 migrations apply DB --remote` then `wrangler deploy`.
- `FRONTEND_ORIGIN` prod: `https://unitutor.askwho.net`.
- LTI/JWKS smoke uses temporary `lti_deployments` row then deletes it — see [[wiki/Engineering/AI-Native-Engineering/UniTutor-LTI-13-B2B.md]].

## 게이트

- Secrets: `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`.
- `prod:` 증거 = public DNS + HTTP 200 (530/NXDOMAIN 아님).
- 첫 원격 closeout: merge `bd40a573` / Actions 37014651191.
