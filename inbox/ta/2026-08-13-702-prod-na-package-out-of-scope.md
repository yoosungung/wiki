---
id: inbox-ta-702-prod-na-package-out-of-scope
agent: ta
ticket_id: 702
updated: 2026-08-13
status: inbox
sources:
  - ticket:702
  - https://github.com/yoosungung/nl2sql/pull/89
  - merge_sha:3296b420c1886805f167b4acb9298a8292107fc1
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# #702 prod_* N/A (package out of scope)

- Gates: test_* #3589 · qa: e2e pass #3597 · aa: security pass #3593 @ tip `test-3296b42`.
- No `deploy.yml` / no separate prod NS apply — Prod package = `publish-releases` semver only (`test-*` forbidden).
- `prod_*` = N/A (package out of scope); tip overlay already smoked. PM Done when §2.8 complete.
