---
id: inbox-pm-nl2sql-test-tip-ghcr-vs-publish
agent: pm
ticket_id: 549
updated: 2026-08-12
status: inbox
sources:
  - ticket:549
  - ticket:391
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - https://oneuptime.com/blog/post/2025-12-20-workflow-dispatch-inputs-github-actions/view
---

# nl2sql Test tip GHCR ≠ publish-releases

- Deploying Test tip roll must use a dedicated `build-ghcr-images` (workflow_dispatch → backend+mcp linux → GHCR only); do not call `publish-releases tag=test-*` (creates unwanted public `test-*` Releases on nl2sql-releases).
- Prod package axis stays `publish-releases`: reuse pre-pushed GHCR images; keep mcp linux/macos assets + README sync; guard/fail on `test-*` tags.
- Aligns with wiki Test overlay vs Release package axes; product SoT is ticket attachment `test-ghcr-image-path.plan.md`.
