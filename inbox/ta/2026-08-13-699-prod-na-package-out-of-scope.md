---
id: inbox-ta-699-prod-na-package-out-of-scope
agent: ta
ticket_id: 699
updated: 2026-08-13
status: inbox
sources:
  - ticket:699
  - https://github.com/yoosungung/nl2sql/pull/87
  - merge_sha:13251b090e5d99da68cffc5f109b49974776bb72
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# #699 prod_* N/A — package out of scope

- After qa: e2e pass (#3529) + aa: security pass (#3541) on tip `test-13251b0` (nl2sql#87 merge `13251b090…`).
- No `deploy.yml`; Prod = `publish-releases` semver only — `test-*` tip tags forbidden.
- No separate prod NS/roll. CD closeout: `prod_* = N/A (package out of scope)` with test_* + qa/aa.
- Hand to pm for Done (§2.8 evidence complete). Optional local007 EX remains EX axis.
