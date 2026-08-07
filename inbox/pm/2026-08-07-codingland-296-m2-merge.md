---
id: inbox-pm-codingland-296-m2-merge
agent: pm
ticket_id: 296
updated: 2026-08-07
status: inbox
sources:
  - ticket:296
  - https://github.com/yoosungung/codingland/pull/3
---

# codingland #296 M2 merge

- PR #3 merged (`aad820e`); M2 Replay sandbox (IsolatedRunner in-process, shallow Sanitizer maxDepth=3, Living Spec scenarioId↔Jest, Time Bar/Hot Reboot host wiring).
- Evidence: `cd extension && npm test` → 11 suites / 37 passed; `npm run compile` clean; no required GH checks.
- tenant_cd/QA/AA: N/A (local extension package) → Done after merge (not Deploying Test/@ta).
