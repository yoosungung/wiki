---
id: inbox-ta-564-prod-na-package-out-of-scope
agent: ta
ticket_id: 564
updated: 2026-08-13
status: inbox
sources:
  - ticket:564
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - https://github.com/yoosungung/nl2sql/blob/main/deploy/SETUP.md
---

# #564 prod_* N/A — package out of scope

- Deploying Prod after QA/AA pass on tip `test-7f519f2` (nl2sql#77).
- Ticket Non-goals exclude Prod overlay; Prod path is `publish-releases` semver only — `test-*` tags forbidden.
- No `deploy.yml` / no separate prod NS. Feature Done uses `prod_* = N/A (package out of scope)` with existing test_* + qa/aa pass.
