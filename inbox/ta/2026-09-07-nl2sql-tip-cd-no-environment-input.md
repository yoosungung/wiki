---
id: inbox-ta-nl2sql-tip-cd-no-environment-input
agent: ta
ticket_id: 1747
updated: 2026-09-07
status: inbox
sources:
  - ticket:1747
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# nl2sql tip CD: no workflow `environment` input

- `tenant-cd-registry.json` may list `inputs.environment`, but `build-ghcr-images.yml` has **no** `environment` input — `gh workflow run -f environment=…` → HTTP **422**.
- Test tip path: Kaniko primary → `tag=test-<shortsha>`; Actions fallback only `-f tag=test-<shortsha> -f backend_multi_arch=false`; then `kubectl set image` **backend only** (keep mcp pin).
- Stale `nl2sql-ghcr-build` github-token → Kaniko `git-clone` Init:Error `403 Write access not granted`; refresh secret from current `GH_TOKEN` + ghcr config.json before retry.
