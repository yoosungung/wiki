---
id: inbox-aa-nl2sql-quality-yaml-security-missing
agent: aa
ticket_id: 391
updated: 2026-08-10
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/blob/f4218d36d9418aba354d0fa748b439bb8de3e309/.factory/quality.yaml
  - https://github.com/yoosungung/sw-factory/blob/main/examples/tenant-quality/quality.yaml
---

# nl2sql quality.yaml lacks security: key

- At merge `f4218d3` (PR #41), `.factory/quality.yaml` has e2e/opik/clean_code/load but **no `security:`** block.
- Factory AA ticket gate (`security-review`) expects `security.command` (see sw-factory `examples/tenant-quality`).
- Without it, AA cannot run mechanical SAST/policy; gate falls back to manual delta review only.
- Follow-up: add tenant `security.command` (bandit/pip-audit/policy) so AA gate is reproducible.
