---
id: inbox-aa-codingland-556-aa-security-pr9-delta
agent: aa
ticket_id: 556
updated: 2026-08-12
status: inbox
sources:
  - ticket:556
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - inbox/aa/2026-08-12-codingland-556-aa-security-vscode-gate.md
  - https://github.com/yoosungung/codingland/pull/9
---

# codingland #556 AA security — PR#9 core-first delta

- Candidate: master `f4ea6cc` (PR #9). Prior pass: `4aa67fb` (PR #8).
- `.factory/quality.yaml`: `e2e` only — no `security.command` → mechanical skip; scoped manual on delta.
- Diff vs prior: `extension/package.json` `test:vscode` → `npm run compile && …` (core then host); `DESIGN.md` Pod deps + core-first docs. Harness (`run-vscode-test.cjs`, download/fallback) **unchanged**.
- No new trust boundary / secrets / network egress. Residual Medium (VSCodium fallback integrity/tar-slip) + Low (`VSCODE_EXECUTABLE_PATH`) still non-blocking; DESIGN now prefers pin.
