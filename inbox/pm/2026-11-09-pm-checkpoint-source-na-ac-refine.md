---
id: inbox-pm-2026-11-09-pm-checkpoint-source-na-ac-refine
agent: pm
ticket_id: 38f15177-82cb-43c9-a7e0-549e9fda9a60
updated: 2026-11-09
status: inbox
sources:
  - ticket:38f15177-82cb-43c9-a7e0-549e9fda9a60
  - ticket:85b94ff9-1aa1-4616-8df6-3c87eef2c01a
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
---

# pm-checkpoint: source N/A = error (AC refine)

- FLOW_COUNT=2 both candidate.win `in_progress` @candidate; review/deploy/qa empty.
- Silence <30m on both → no stall / no Approval; `in_progress_empty=0/3`.
- eric on `38f15177`: missing source is itself an error after agent judgment; regression suspected post sw-factory migration (old posts OK).
- PM actionable: AC refine → primary fix SSoT/curation URL; render-hide N/A is secondary defense.
- Boards seeded (`<!-- pm-checkpoint-status -->`) on both flow tickets; actionable add_comment=1.
