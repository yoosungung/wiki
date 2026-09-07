---
id: inbox-ta-nl2sql-kaniko-ghcr-secret
agent: ta
ticket_id: 1747
updated: 2026-09-07
status: inbox
sources:
  - ticket:1747
  - /tmp/tenant-repos/nl2sql/deploy/SETUP.md
---

# nl2sql Kaniko tip: stale `nl2sql-ghcr-build` token → Init:Error 403

- Symptom: Kaniko tip Jobs `Init:Error` on `git-clone`; log `remote: Write access to repository not granted` / HTTP 403 to `yoosungung/nl2sql`.
- Cause: Secret `nl2sql/nl2sql-ghcr-build` key `github-token` expired or lost Contents:Read on the private repo.
- Fix (TA): recreate secret per SETUP.md (github-token + ghcr.io config.json), then re-run `./deploy/scripts/build-tip-images-kaniko.sh test-<shortsha> main`.
- Tip roll: backend image only to `ghcr.io/yoosungung/nl2sql-backend:test-<sha>`; do not retarget mcp binary annotation to `test-*`.
