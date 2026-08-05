---
id: inbox-sw-factory-2026-08-05-ticket199-design-recovery
agent: sw-factory
ticket_id: 199
updated: 2026-08-05
status: inbox
sources:
  - ticket:199
  - ticket:197
  - agent-runner/DESIGN.md
  - ARCHITECTURE.md §2.3.1
  - https://cursor.com/docs/sdk/typescript
---

# #199 DESIGN § Recovery R1–R5

- Canonical AC for zombie `active_run` lives in `agent-runner/DESIGN.md` § Recovery (parent #197 R1–R5).
- HTTP dialect unchanged: 202 accepted / 409 `skipped_active_run`; recovery is parent/pool internal (`session.recover` log).
- Default consecutive skip threshold=2; missing SDK cancel → DELETE session + forget satisfies R3.
- Impl+tests are #200; docs-only #199 lands DESIGN + ROADMAP checkbox + §2.3.1 pointer.
