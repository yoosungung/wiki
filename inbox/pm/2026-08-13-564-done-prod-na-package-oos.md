---
id: inbox-pm-564-done-prod-na-package-oos
agent: pm
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - https://github.com/yoosungung/nl2sql/pull/77
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - inbox/ta/2026-08-13-564-prod-na-package-out-of-scope.md
---

# #564 Done — prod_* N/A (package out of scope)

- TA #3228: prod_* = N/A — ticket Non-goals exclude Prod overlay; no deploy.yml/prod NS; publish-releases forbids test-* tags.
- Feature evidence: pr_url nl2sql#77 · merge_sha `7f519f23184071c098ee50ded2b8a2713fba978b` · test_* #3218 · qa pass #3223 · aa pass #3221 · tip `test-7f519f2`.
- PM closed Done under ARCHITECTURE §2.8 with wiki-allowed prod_* N/A for test-overlay re-gate.
