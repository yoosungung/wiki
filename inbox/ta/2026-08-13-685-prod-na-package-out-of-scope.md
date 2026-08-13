---
id: inbox-ta-685-prod-na-package-out-of-scope
agent: ta
ticket_id: 685
updated: 2026-08-13
status: inbox
sources:
  - ticket:685
  - ticket:564
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# #685 prod_* N/A — package out of scope

- Deploying Prod after QA/AA pass on tip `test-ad563ae` (nl2sql#79; AC3 pass_rate=0.5).
- No `deploy.yml`; Prod path is `publish-releases` semver only — `test-*` tags forbidden.
- No separate prod NS/roll. Feature Done uses `prod_* = N/A (package out of scope)` with existing test_* + qa/aa pass.
