---
id: inbox-pm-1749-xvfb-soft-skip-merge
agent: pm
ticket_id: 1749
updated: 2026-09-07
status: inbox
sources:
  - ticket:1749
  - https://github.com/yoosungung/codingland/pull/13
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
---

# #1749 merged — xvfb soft-skip for EH smoke

- PR #13 merged (`merge_sha=e24cec149dfa71c8c5c026749fbc4ce9f4d73444`): `xvfbGuard` soft-skips `test:vscode` when Linux headless lacks `xvfb-run`; unit remains clean_code floor.
- PM review trimmed DESIGN.md layout rows for non-existent `runnerTape`/`workspaceGraphMerge` (scope drift from parallel NF).
- codingland has no tenant_cd (VSIX dogfood) — Done after merge; no Deploying Test/@ta.
