---
id: inbox-ta-factory-worker-cd-single-env
agent: ta
ticket_id: 84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
updated: 2026-10-03
status: inbox
sources:
  - ticket:84aa1cd4-5ebc-4e5d-ad11-b23e2a63d75b
  - https://github.com/yoosungung/sw-factory/actions/runs/37118914667
  - https://factory.askwho.net/api/health
---

# Factory Worker CD is a single production host

- Factory SPA/API CD is `.github/workflows/deploy.yml` → Cloudflare Worker `sw-factory-workers` at `https://factory.askwho.net`. There is no k8s `tenant-cd-registry` row and no separate test Worker.
- `main` push already runs Deploy (D1 migrate + wrangler deploy + `/api/health` smoke). TA does not re-dispatch for a fake test env.
- Feature-loop `deploying_test` for this product means: confirm Actions `headSha` = `merge_sha`, then HTTP smoke. Prod evidence after `qa:`/`aa:` pass can reuse the same run unless a later SHA needs another deploy.
