---
id: inbox-ta-1272-prod-package-na-metadata
agent: ta
ticket_id: 1272
updated: 2026-08-25
status: inbox
sources:
  - ticket:1272
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# Deploying Prod after metadata-only tip loop → prod_* N/A

- When merge delta is metadata/fixtures only (no RELEASE.md/semver bump), shared-cluster tip (`test-<sha>` Kaniko + tip_roll) is the Test axis; **Prod package** (`build-ghcr` semver + `publish-releases`) is out of scope.
- Feature evidence: keep full `test_*` + `qa:`/`aa:` pass; set `prod_* = N/A (package out of scope)` — do not invent a version tag or tip→prod rewrite.
- Tip tags must not feed `publish-releases` (wiki In-Cluster-Kaniko-Tip-GHCR).
