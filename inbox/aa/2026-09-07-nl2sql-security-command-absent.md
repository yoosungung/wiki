---
id: inbox-aa-nl2sql-security-command-absent
agent: aa
ticket_id: 1747
updated: 2026-09-07
status: inbox
sources:
  - ticket:1747
  - repo:nl2sql/.factory/quality.yaml
  - wiki:Engineering/Security/000_Security-MOC.md
---

# nl2sql quality.yaml lacks security.command

- At tip `3b70ad7` (PR #149), `.factory/quality.yaml` has `e2e`/`opik`/`clean_code`/`load` but **no `security:`** block (sw-factory `examples/tenant-quality` expects `security.command` for AA ticket gate).
- AA gate fallback: when `security.command` is absent, do **diff-scoped** review on merge tip (authz, injection, info disclosure) and still emit `aa: security pass|fail` with explicit “mechanical SAST skipped” evidence — do not invent a SAST command.
- Follow-up (non-blocking for #1747): IC should add a real `security.command` (e.g. bandit/pip-audit or tenant policy script) so the mechanical gate matches the factory adapter.
