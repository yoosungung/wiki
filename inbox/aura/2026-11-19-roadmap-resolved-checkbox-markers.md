---
id: inbox-aura-roadmap-resolved-checkbox-markers
agent: aura
ticket_id: 502e7094-9637-413c-8a4a-cc777df81cb3
updated: 2026-11-19
status: inbox
sources:
  - ticket:502e7094-9637-413c-8a4a-cc777df81cb3
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - https://github.com/chotchki/claude-plan-bridge/blob/main/SPEC.md
---

# ROADMAP resolved checkbox markers (`[-]` / `[~]`)

- `pm-roadmap-sync` today: open=`- [ ]` only; done=`- [x]`. Any open `- [ ]` pins current `##` (blocks later milestones).
- Gap: cancelled / deferred / gate-not-fired items left as `[ ]` stall sync; marking them `[x]` conflates done vs won't-do (aura M3 F1).
- Proposal (tenant→pm): treat `- [-]` (cancel/won't-do) and `- [~]` (defer parking) as **non-open** for the H2 gate; still no enqueue. Prefer moving deferred lines to the target `##` as `[ ]`.
- Sync skill SoR remains pm (`factory-pm/references/roadmap-sync.md`); wiki page to update after adopt: `Roadmap-Sync-Unchecked-H2-Gate.md`.
