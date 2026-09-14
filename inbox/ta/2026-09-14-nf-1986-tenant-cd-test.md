---
id: inbox-ta-nf-1986-tenant-cd-test
agent: ta
ticket_id: 1986
updated: 2026-09-14
status: inbox
sources:
  - ticket:1986
  - https://github.com/yoosungung/nl2sql/pull/151
---

# nl2sql #1986 Deploying Test tip (Kaniko)

- Tip primary path: in-cluster Kaniko backend Job → GHCR `test-<shortsha>` → `kubectl set image` on `nl2sql/nl2sql-backend` (do not retarget mcp binary pin to `test-*`).
- merge_sha `50e2b81` → tag `test-50e2b81`; Job `nl2sql-kaniko-backend-test-50e2b81` Complete; smoke `/api/health`+`/api/ready` 200 after roll.
- Actions `build-ghcr-images.yml` remains fallback; registry `environment` input is unused by that workflow (tag-only).
