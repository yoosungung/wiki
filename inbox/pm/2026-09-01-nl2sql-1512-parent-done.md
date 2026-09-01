---
id: inbox-pm-nl2sql-1512-parent-done
agent: pm
ticket_id: 1512
updated: 2026-09-01
status: inbox
sources:
  - ticket:1512
  - ticket:1514
  - https://github.com/yoosungung/nl2sql-releases/releases/tag/v0.1.4
---

# nl2sql #1512 parent Done after #1514 linux-only

- Parent Prod package release closed when both children Done (#1513 GHCR, #1514 nl2sql-releases v0.1.4 linux-amd64).
- Dual-loop test/qa/aa/prod evidence = N/A for package_manual (no tenant_cd cluster apply).
- macOS asset skipped this cut per Eric #6159; residual publish-releases workflow green is hygiene only.
