---
id: inbox-ta-2026-08-06-ticket172-prod-841059f-package
agent: ta
ticket_id: 172
updated: 2026-08-06
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/pull/38
  - https://github.com/yoosungung/nl2sql/actions/runs/31065462440
  - https://github.com/yoosungung/nl2sql-releases/releases/tag/prod-841059f
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# nl2sql #172 prod package via publish-releases

- Deploying Prod after QA #748 smoke PASS + AA #740 security pass on `test-841059f`.
- No prod kustomize overlay; prod_* = release package axis (`publish-releases` tag `prod-841059f`) — not cluster apply.
- merge_sha `841059f5178bce8f239d2a6de96423b0b371e98e` → GHCR `nl2sql-backend:prod-841059f` / `nl2sql-mcp:prod-841059f` + releases assets linux/macos.
- Test NS left on validated `test-841059f`; MDL PVC HEAD `5fe07689…` kept (no reseed); mcp deploy unchanged.
