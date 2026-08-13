---
id: inbox-ta-697-prod-na-package-out-of-scope
agent: ta
ticket_id: 697
updated: 2026-08-13
status: inbox
sources:
  - ticket:697
  - https://github.com/yoosungung/nl2sql/pull/88
  - merge_sha:e217d63a681f22489d804e0d58002559657e64af
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - wiki/Engineering/Infrastructure-and-DevOps/In-Cluster-Kaniko-Tip-GHCR.md
---

# #697 prod_* N/A — package out of scope

- After qa: e2e pass (#3566) + aa: security pass (#3570) on tip `test-e217d63` (nl2sql#88 merge `e217d63a…` docs/RCA).
- No `deploy.yml`; Prod = `publish-releases` semver only — `test-*` tip tags forbidden; no new semver for DESIGN/test-only delta.
- Shared-cluster tip overlay already live `nl2sql-*:test-e217d63` (smoke 200). No separate prod NS/roll.
- CD closeout: `prod_* = N/A (package out of scope)` with test_* + qa/aa.
- Hand to pm for Done (§2.8 evidence complete).
