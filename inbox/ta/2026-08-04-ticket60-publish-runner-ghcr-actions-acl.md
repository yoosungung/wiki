---
id: inbox-ta-ticket60-publish-runner-ghcr-actions-acl
agent: ta
ticket_id: 60
updated: 2026-08-04
status: inbox
sources:
  - ticket:60
  - https://github.com/yoosungung/sw-factory/actions/runs/30871649252
  - inbox/ta/2026-08-04-ticket60-deploying-test-ghcr-blocker.md
  - https://stackoverflow.com/questions/70646920/github-token-permission-denied-write-package-when-build-and-push-docker-in-github-workflows
---

# #60 publish-runner GHCR 403 — Actions package ACL

- `publish-runner.yml` has `permissions: packages: write`; login to GHCR succeeds; build succeeds.
- Push fails: `HEAD …/blobs/sha256:… 403 Forbidden` on `ghcr.io/yoosungung/cursor-agent-runner:latest`.
- Likely cause: package created earlier with PAT → Actions repo not in package **Manage Actions access** (Write).
- Fix (human): grant `yoosungung/sw-factory` Write on the package, or delete package and let Actions recreate it.
- After fix: re-run workflow → `kubectl -n sw-factory rollout restart statefulset -l app=cursor-agent` → verify live MCP `get_status_labels(project_id=5)`.
