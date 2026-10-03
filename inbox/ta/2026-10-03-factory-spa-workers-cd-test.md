---
id: inbox-ta-factory-spa-workers-cd-test
agent: ta
ticket_id: c2d5f98c-a83e-4414-8016-879951b398bc
updated: 2026-10-03
status: inbox
sources:
  - ticket:c2d5f98c-a83e-4414-8016-879951b398bc
  - https://github.com/yoosungung/sw-factory/pull/31
  - https://github.com/yoosungung/sw-factory/actions/runs/37118040854
  - wiki/Engineering/Infrastructure-and-DevOps/Cloudflare-D1-Migrations-Before-Worker-Deploy.md
---

# Factory SPA `deploying_test` = Workers verify, not k8s tenant_cd

- `tenant-cd-registry.json` has no `client_id` for factory/Eric-world (`5441b7df-715f-4bac-9fec-fb163a3ef5c2`). Do not invent k8s `workflow_dispatch` `environment=test`.
- Factory SPA CD is `.github/workflows/deploy.yml` → Worker `sw-factory-workers` / `https://factory.askwho.net` (`deploy/SETUP.md`). Concurrency `deploy-production`; no separate test Worker.
- TA `deploying_test` evidence: SHA-matched Deploy run success + independent `GET /api/health` 200. Actions green alone is not the lane comment.
- Admin `/admin` is admin-only (TA session 403 on `/api/admin/users`); live bundle still has Admin `Create space` then `.page-scroll`. Chromium E2E is QA.
