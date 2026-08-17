---
id: inbox-ta-nl2sql-tenant-cd-missing-deploy-yml
agent: ta
ticket_id: 918
updated: 2026-08-16
status: inbox
sources:
  - ticket:918
  - https://github.com/yoosungung/nl2sql/pull/107
  - tenant-cd-registry.json (client_id=3 / repo_id=nl2sql)
---

# nl2sql tenant_cd: registry deploy.yml missing on main

- `~/.cursor/tenant-cd-registry.json` for client_id=3 / repo_id=nl2sql points to `workflow=deploy.yml`, `image_input=image_tag`, verify ns/deploy `nl2sql`.
- On `yoosungung/nl2sql` main (merge_sha `85cba02`), `.github/workflows/` has only `build-ghcr-images.yml`, `ci.yml`, `publish-releases.yml` — no `deploy.yml`.
- `gh workflow run deploy.yml` fails: `workflow deploy.yml not found on the default branch`.
- Product tip path (comment in `build-ghcr-images.yml`): dispatch `tag=test-<sha>` then kubectl tip roll via `deploy/k8s/overlays/test/` — not the registry contract; TA must not invent alternate workflow until registry or product adds `deploy.yml`.
- Ticket #918 Deploying Test blocked until registry↔repo CD contract is fixed (platform) or `deploy.yml` lands (product).
