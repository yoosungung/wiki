---
id: inbox-nl2sql-2026-08-13-mcp-binary-no-test-tip
agent: nl2sql
ticket_id: 590
updated: 2026-08-13
status: inbox
sources:
  - ticket:590
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# Tip roll must not set mcp-binary to test-*

- Shared-cluster mcp uses `nl2sql-releases` initContainer pin (`v*`/`prod-*` + sha256), not GHCR tip tags.
- `publish-releases` rejects `test-*`; rewriting live `nl2sql.io/mcp-binary` / `patch-mcp-binary.yaml` to `test-<sha>` → init curl HTTP 404 → Init:Error / ProgressDeadlineExceeded while old Ready replica keeps serving.
- Tip roll: change backend (optional private mcp) image tag only; keep published mcp binary pin. Recovery: re-apply `deploy/k8s/overlays/test` (git pin is already `v0.1.3`).
