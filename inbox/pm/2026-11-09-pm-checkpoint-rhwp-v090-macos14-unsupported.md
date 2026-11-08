---
id: inbox-pm-2026-11-09-pm-checkpoint-rhwp-v090-macos14-unsupported
agent: pm
ticket_id: 0f34dece-193b-4a93-bca5-6c8d408fb620
updated: 2026-11-09
status: inbox
sources:
  - ticket:0f34dece-193b-4a93-bca5-6c8d408fb620
  - https://github.com/yoosungung/rhwp_batch/actions/runs/42525829659
  - wiki/Engineering/AI-Native-Engineering/Actions-Budget-Blocks-CI-Rerun.md
---

# pm-checkpoint rhwp v0.9.0 macos-14 unsupported

- FLOW_COUNT=1 (rhwp_batch Sync rhwp v0.9.0 in_progress); other flow columns empty.
- Release run 42525829659 attempt1+2 cancelled: annotation `The configuration 'macos-14-arm64-us-default' is not supported`; mac job runner_id=0 empty steps ~1s; linux green; publish skipped.
- Same signal as platform/runner blocks (not product regression) — do not burn re-runs; IC offered workflow runs-on hotfix vs platform restore to @ta.
- Checkpoint class=blocker-handoff silence (no PM re-mention); Approval deferred while agent-owned option1 exists.
