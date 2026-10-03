---
id: inbox-ta-factory-prod-cd-descendant-sha
agent: ta
ticket_id: c2d5f98c-a83e-4414-8016-879951b398bc
updated: 2026-10-03
status: inbox
sources:
  - ticket:c2d5f98c-a83e-4414-8016-879951b398bc
  - https://github.com/yoosungung/sw-factory/blob/main/.github/workflows/deploy.yml
---

# Factory prod CD uses current main, not older merge_sha

- Factory `deploy.yml` is single production Worker (`factory.askwho.net`). No `environment` input; k8s `tenant-cd-registry` has no sw-factory row.
- After qa/aa pass, TA `workflow_dispatch` on **current `main`** if it already contains the ticket `merge_sha`. Re-dispatching the older `merge_sha` would roll back later merges.
- `prod_rollout`: N/A k8s — wrangler Worker. Smoke: `GET /api/health`.
