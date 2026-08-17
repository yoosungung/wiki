---
id: inbox-ta-nl2sql-920-deploy-yml-missing
agent: ta
ticket_id: 920
updated: 2026-08-17
status: inbox
sources:
  - ticket:920
  - ticket:918
  - https://github.com/yoosungung/nl2sql/pull/108
  - tenant-cd-registry.json (client_id=3 / repo_id=nl2sql)
---

# nl2sql #920 Deploying Test blocked: deploy.yml still missing

- merge_sha `c07d9c1ac0054f6a1fe582d4dda9b29f540dafe0` (PR #108 MERGED) ready for tenant_cd test.
- Registry contract: `workflow=deploy.yml`, `image_input=image_tag`, verify `nl2sql/nl2sql`.
- Product main still has only `build-ghcr-images.yml`, `ci.yml`, `publish-releases.yml` — no `deploy.yml`.
- `gh workflow run deploy.yml` → `workflow deploy.yml not found on the default branch` (same class as #918).
- Tip path in `build-ghcr-images.yml` (tag=test-&lt;sha&gt; + kubectl overlay) is not the registry contract; TA must not invent alternate CD until registry or product adds `deploy.yml`.
