---
id: inbox-ta-2026-08-06-ticket172-prod-841059f-publish
agent: ta
ticket_id: 172
updated: 2026-08-06
status: inbox
sources:
  - ticket:172
  - https://github.com/yoosungung/nl2sql/actions/runs/31065462440
  - https://github.com/yoosungung/nl2sql-releases/releases/tag/prod-841059f
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
---

# nl2sql #172 prod package publish (prod-841059f)

- Prod axis = release package publish (not cluster apply). Test NS left on `test-841059f`; MDL keep; mcp deploy unchanged.
- `Publish to nl2sql-releases` run 31065462440 success on merge_sha `841059f5178bce8f239d2a6de96423b0b371e98e` → tag `prod-841059f` with mcp linux/macos assets + GHCR `nl2sql-backend`/`nl2sql-mcp` images.
- tenant_cd registry still lists missing `deploy.yml`; live path remains publish-releases + (test-only) overlay set-image.
