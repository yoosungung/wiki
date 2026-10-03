---
id: factory-workers-single-env-cd
title: "Factory SPA/API CD: Workers 단일 prod (test env 없음)"
status: canonical
owner: km
updated: "2026-10-04"
review_after: "2027-01-04"
sources:
  - inbox/ta/2026-10-03-factory-workers-single-env-cd.md
  - inbox/ta/2026-10-03-factory-spa-workers-cd-test.md
  - inbox/ta/2026-10-03-factory-worker-cd-single-env.md
  - inbox/ta/2026-10-03-factory-prod-cd-descendant-sha.md
  - inbox/ta/2026-10-03-factory-newest-first-prod.md
  - ticket:c2d5f98c-a83e-4414-8016-879951b398bc
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
  - https://github.com/yoosungung/sw-factory/blob/main/.github/workflows/deploy.yml
  - wiki/Engineering/Infrastructure-and-DevOps/Cloudflare-D1-Migrations-Before-Worker-Deploy.md
  - wiki/Engineering/Infrastructure-and-DevOps/Tenant-CD-Registry-Missing-Workflow.md
tags: ["Engineering", "Infrastructure", "Factory", "Cloudflare", "CD"]
type: "wiki"
---

# Factory SPA/API CD: Workers 단일 prod (test env 없음)

## SoR

- CD: `.github/workflows/deploy.yml` (`push` main + `workflow_dispatch`) → Worker `sw-factory-workers` / `https://factory.askwho.net`.
- **`environment` input 없음**. concurrency `deploy-production`.
- `tenant-cd-registry.json`에 factory/Eric-world(`5441b7df-…`) **행 없음** — k8s `environment=test`를 발명하지 말 것([[wiki/Engineering/Infrastructure-and-DevOps/Tenant-CD-Registry-Missing-Workflow.md]]).

## Lane 해석

| 상태 | TA 증거 |
| --- | --- |
| `deploying_test` | SHA-matched Deploy 성공 + 독립 `GET /api/health` 200. Actions green alone ≠ lane comment. |
| prod | qa/aa 이후. `main`이 이미 ticket `merge_sha`를 포함하면 **현재 main** Deploy를 재사용 — 옛 SHA `workflow_dispatch`는 later merges 롤백. |

## 함정

- Admin `/admin`은 admin-only(TA 세션 `/api/admin/users` 403 가능) — 번들 레이아웃 스모크와 Chromium E2E(QA)를 혼동하지 말 것.
- D1 migrate 순서: [[wiki/Engineering/Infrastructure-and-DevOps/Cloudflare-D1-Migrations-Before-Worker-Deploy.md]].
