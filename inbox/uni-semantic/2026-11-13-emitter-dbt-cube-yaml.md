---
id: inbox-uni-semantic-emitter-dbt-cube-yaml
agent: uni-semantic
ticket_id: 51c758f3-2047-4ba1-a3df-c102550f5a9b
updated: 2026-11-13
status: inbox
sources:
  - ticket:51c758f3-2047-4ba1-a3df-c102550f5a9b
  - https://docs.getdbt.com/docs/build/semantic-models
  - https://docs.cube.dev/docs/data-modeling/concepts/syntax
---

# uni-semantic Phase 4 Emitter MVP (dbt · Cube)

- Hub-only emitters: `backends/dbt` → MetricFlow standalone YAML (`semantic_models` + `metrics`); `backends/cube` → Cube YAML (`cubes`).
- Min IR input matches Looker emitter: `table` (+pk/fk), `metric` `sum|count|avg(col)`, optional `view` joins.
- dbt uses legacy MetricFlow YAML (not model-embedded latest spec) so a single emit artifact does not require a dbt DAG.
- Cube joins from `view` (base=table) else `table.fk`; relationship fixed `many_to_one`.
- Non-goals on same ticket: MCP, `slg` packaging, GUI Schema Diff, IR schema patch.
