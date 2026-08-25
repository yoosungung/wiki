---
id: inbox-ta-1272-tenant-cd-tip-tag
agent: ta
ticket_id: 1272
updated: 2026-08-25
status: inbox
sources:
  - ticket:1272
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
  - wiki/Engineering/Infrastructure-and-DevOps/Tip-Roll-Keep-Published-Binary.md
---

# nl2sql tenant_cd tip path uses tag=test-&lt;sha&gt;

- `build-ghcr-images.yml` has **no** `environment` input; registry `inputs.environment` causes HTTP 422.
- Deploying Test tip: `gh workflow run build-ghcr-images.yml -f tag=test-<shortsha> -f backend_multi_arch=false` then `kubectl set image` tip roll (container name, keep mcp binary pin).
- Sakila refSql seals land via metadata FS PUT (`sync.status=ok`); product merge SHA ≠ metadata `last_good_ref`.
