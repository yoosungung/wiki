---
id: uni-semantic-phase4-emitter
title: "uni-semantic Phase 4: Emitter MVP (dbt · Cube) + MCP/slg backlog"
status: canonical
owner: km
updated: "2026-11-14"
last_updated: "2026-11-14"
review_after: "2027-02-14"
sources:
  - inbox/uni-semantic/2026-11-13-emitter-dbt-cube-yaml.md
  - inbox/pm/2026-11-13-emitter-dbt-cube-intent-pass.md
  - inbox/pm/2026-11-13-uni-semantic-emitter-intent-pass.md
  - inbox/pm/2026-11-13-uni-semantic-phase4-kickoff.md
  - inbox/pm/2026-11-13-pm-checkpoint-uni-semantic-phase4-quiet.md
  - inbox/pm/2026-11-13-pm-checkpoint-uni-semantic-phase4-quiet2.md
  - inbox/pm/2026-11-13-pm-checkpoint-uni-semantic-phase4-empty1.md
  - inbox/pm/2026-11-13-pm-checkpoint-uni-semantic-phase4-empty1b.md
  - inbox/pm/2026-11-13-pm-checkpoint-uni-semantic-phase4-empty2.md
  - inbox/pm/2026-11-13-pm-checkpoint-uni-semantic-phase4-empty2b.md
  - inbox/pm/2026-11-13-pm-checkpoint-uni-semantic-phase4-empty3.md
  - inbox/pm/2026-11-13-pm-checkpoint-uni-semantic-phase4-empty3b.md
  - ticket:ba31c9e8-b3a9-43a4-948a-fe02ded277e3
  - ticket:51c758f3-2047-4ba1-a3df-c102550f5a9b
  - ticket:d15d16f2
  - ticket:9abce257
  - https://docs.getdbt.com/docs/build/semantic-models
  - https://docs.cube.dev/docs/data-modeling/concepts/syntax
tags: ["Engineering", "uni-semantic", "Phase4", "Emitter", "dbt", "Cube"]
type: wiki
---

# uni-semantic Phase 4: Emitter MVP (dbt · Cube)

Parent milestone `ba31c9e8` — ROADMAP `## Phase 4 — 에코시스템 · MCP · slg 배포`. `tenant_cd` N/A → Done = merge + local `cargo test` 증거.

## Kickoff

- Eric Approval (`@pm 시작 해`) → milestone `waiting_for_approval` → `in_progress`.
- First slice: Emitter `51c758f3` → lane developer; MCP `d15d16f2` / `slg` `9abce257` stay backlog until Emitter seals.

## Emitter MVP (Intent pass · PR #16)

- Hub-only: `backends/dbt` → MetricFlow **standalone** YAML (`semantic_models` + `metrics`); `backends/cube` → Cube YAML (`cubes`).
- Min IR = Looker emitter: `table` (+pk/fk), `metric` `sum|count|avg(col)`, optional `view` joins. **No IR schema patch.**
- dbt: legacy MetricFlow YAML (not model-embedded) so one emit artifact ≠ dbt DAG requirement.
- Cube joins: `view` (base=table) else `table.fk`; relationship fixed `many_to_one`.
- Non-goals on Emitter ticket: MCP, `slg` packaging, GUI Schema Diff.
- Verify: `cargo test -p backend_dbt -p backend_cube` (4 unit) + full `cargo test` green; ROADMAP first Phase 4 checkbox `[x]`.

## pm-checkpoint silence (post-Emitter)

- FLOW often = milestone only in_progress; review/deploy/qa empty.
- Silence ≥30m × 3 empty → `waiting_for_approval` + `@eric.yoo` (MCP/`slg` kickoff waits human).
- Board-only / status-board upsert does **not** reset silence clock.

## 관련

- Phase 3 closeout: [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Phase3-Dialect-and-Spokes.md]]
- Roadmap sync: [[wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md]]
- Checkpoint ops: [[wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md]]
