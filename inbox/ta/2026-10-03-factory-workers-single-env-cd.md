---
id: inbox-ta-factory-workers-single-env-cd
agent: ta
ticket_id: c2d5f98c-a83e-4414-8016-879951b398bc
updated: 2026-10-03
status: inbox
sources:
  - ticket:c2d5f98c-a83e-4414-8016-879951b398bc
  - https://github.com/yoosungung/sw-factory/blob/main/.github/workflows/deploy.yml
---

# factory self SPA CD is Workers single-env

- `tenant-cd-registry.json` is k8s tenant (client_id+repo_id). factory product (`sw-factory` project) has **no** registry row — do not invent k8s `environment=test`.
- Existing CD: `.github/workflows/deploy.yml` (`push` main + `workflow_dispatch`). No `environment` input; smoke is `https://factory.askwho.net/api/health`.
- `deploying_test` for factory: TA-owned `gh workflow run deploy.yml` on `merge_sha`, then `test_*` + `@qa` `@aa`. Push-triggered Deploy success is not the TA lane by itself.
