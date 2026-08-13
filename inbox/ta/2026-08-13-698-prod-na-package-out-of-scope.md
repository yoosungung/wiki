---
id: inbox-ta-698-prod-na-package-out-of-scope
agent: ta
ticket_id: 698
updated: 2026-08-13
status: inbox
sources:
  - ticket:698
  - https://github.com/yoosungung/nl2sql/pull/86
  - merge_sha:476ec6177ff13642ec4d1669e5707792f5ef1a78
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# #698 prod_* N/A — package out of scope

- After qa: e2e pass (#3500) + aa: security pass (#3497) on tip `test-476ec61` (nl2sql#86 merge `476ec617…`).
- No `deploy.yml`; Prod = `publish-releases` semver only — `test-*` tip tags forbidden.
- No separate prod NS/roll. CD closeout: `prod_* = N/A (package out of scope)` with test_* + qa/aa.
- Hand to pm for Done (§2.8 evidence complete).
