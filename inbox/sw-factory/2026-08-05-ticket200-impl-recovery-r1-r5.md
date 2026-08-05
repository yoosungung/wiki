---
id: inbox-sw-factory-2026-08-05-ticket200-impl-recovery
agent: sw-factory
ticket_id: 200
updated: 2026-08-05
status: inbox
sources:
  - ticket:200
  - ticket:197
  - ticket:199
  - agent-runner/DESIGN.md
  - https://cursor.com/docs/sdk/typescript
  - https://github.com/yoosungung/sw-factory/pull/3
---

# #200 impl: zombie active_run recovery + tests

- R1–R5 live in `session-manager`/`worker-pool`; tests `agent-runner/tests/session-recover.test.ts`.
- HTTP dialect unchanged (409 `skipped_active_run`); recovery is internal + `session.recover` logs.
- Missing SDK cancel handle → `DELETE` session + forget satisfies R3 (DESIGN); `run.cancel` / `Agent.cancelRun` when handle known.
- Verify: `AGENT_RUNNER_MOCK=1 npm test` green; PR https://github.com/yoosungung/sw-factory/pull/3
