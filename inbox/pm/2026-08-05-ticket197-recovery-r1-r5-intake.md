---
id: inbox-pm-2026-08-05-ticket197-recovery-intake
agent: pm
ticket_id: 197
updated: 2026-08-05
status: inbox
sources:
  - ticket:197
  - inbox/sw-factory/2026-08-05-agent-runner-zombie-active-run.md
  - https://github.com/yoosungung/sw-factory/blob/main/agent-runner/DESIGN.md
  - https://github.com/yoosungung/sw-factory/blob/main/ARCHITECTURE.md
---

# #197 Recovery R1–R5 intake

- Parent intake filled: Goal / Non-goals / AC R1–R5 / Risks / test evidence / Architecture notes (HTTP §2.3.1 unchanged).
- Canonical subtasks: #199 docs DESIGN § Recovery (In Progress); #200 impl+tests (New). Dupes #201/#202 Archived.
- Default consecutive `skipped_active_run` threshold=2; SDK cancelRun missing → DELETE session + forget satisfies R3.
- Evidence: `AGENT_RUNNER_MOCK=1 npm test`; tenant_cd Done gate N/A (framework merge → Review→Done).
