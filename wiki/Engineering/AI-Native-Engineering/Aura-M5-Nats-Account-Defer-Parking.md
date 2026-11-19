---
id: aura-m5-nats-account-defer-parking
title: "ROADMAP [~] defer parking · parent Done blocked by open backlog"
status: canonical
owner: km
updated: "2026-11-20"
last_updated: "2026-11-20"
review_after: "2027-02-20"
sources:
  - inbox/pm/2026-11-19-aura-nats-account-defer.md
  - inbox/pm/2026-11-19-aura-m5-closeout-nats-defer.md
  - inbox/pm/2026-11-19-pm-checkpoint-aura-m5-nats-approval.md
  - ticket:e6ea164f-a2bd-4d8b-8603-fea2d0e83bea
  - ticket:e2df4d9a-6355-4477-9b19-3565020b48f9
  - https://github.com/yoosungung/aura/pull/62
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md
tags: ["Engineering", "ROADMAP", "Defer", "Factory"]
type: wiki
---

# ROADMAP [~] defer parking · parent Done blocked by open backlog

- Human defer of a residual item: author `- [ ]` → `- [~]` (temporary parking; not open for sync incomplete/`- [ ]` gate).
- Do **not** invent kickoff for post-launch parking; route residual open child to `waiting_for_approval` + human when wording is «출시 후».
- Parent mile Done only after deferred child is closed (done + not-implemented note) — open backlog child blocks parent Done.
- `[~]` is temporary — permanent abandon forbidden; later cut-paste into a real future `##`.
- When no next `###` after last passed H2 → pass-gate reply is **no next ###**; freeze until a future H2/H3 appears.

## Related

- [[wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md]]
- [[wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md]]
