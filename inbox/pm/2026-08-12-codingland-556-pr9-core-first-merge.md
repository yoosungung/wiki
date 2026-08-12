---
id: inbox-pm-codingland-556-pr9-core-first-merge
agent: pm
ticket_id: 556
updated: 2026-08-12
status: inbox
sources:
  - ticket:556
  - https://github.com/yoosungung/codingland/pull/9
---

# codingland #556 PR#9 merge (test:vscode core-first)

- QA fail root cause: `test:vscode` compiled host only → fresh sync missing `core/dist` → `Cannot find module '@codingland/core'`.
- Fix merged: `extension/package.json` `test:vscode` → `npm run compile && …` (core then host); DESIGN docs Pod OS deps + core-first contract.
- merge_sha: `f4ea6cc1a15810eefb451fd74beda8facdf71361` (PR #9).
- Deploying Test / TA CD: N/A for this ticket — Extension Host QA gate only (not a Deploying Test URL); post-merge → QA status + qa/aa parallel.
