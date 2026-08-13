---
id: inbox-ta-690-prod-na-package-out-of-scope
agent: ta
ticket_id: 690
updated: 2026-08-13
status: inbox
sources:
  - ticket:690
  - https://github.com/yoosungung/nl2sql/pull/83
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# #690 prod_* N/A — package out of scope

- After qa: e2e pass (#3391) + aa: security pass (#3382) on tip `test-656d0d7` (nl2sql#83 merge `656d0d73…`).
- No `deploy.yml`; Prod path is `publish-releases` semver only — `test-*` tags forbidden (wiki tip overlay).
- No separate prod NS/roll. CD closeout: `prod_* = N/A (package out of scope)` with existing test_* + qa/aa.
- NF EX still pass_rate 0 (#3389) — feature Done blocked on Eric stash/emit (#3390); CD closeout ≠ Done.
