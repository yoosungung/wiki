---
id: uni-semantic-phase3-dialect-and-spokes
title: "uni-semantic Phase 3: Dialect Transpiler · Unresolved · MSTR · Spotfire"
status: canonical
owner: km
updated: "2026-11-13"
last_updated: "2026-11-13"
review_after: "2027-02-13"
sources:
  - inbox/uni-semantic/2026-11-13-dialect-transpiler.md
  - inbox/uni-semantic/2026-11-13-dialect-transpiler-classifier.md
  - inbox/uni-semantic/2026-11-12-dialect-transpiler-classifier.md
  - inbox/uni-semantic/2026-11-13-unresolved-compile-report.md
  - inbox/uni-semantic/2026-11-13-mstr-metadata-schema-json.md
  - inbox/uni-semantic/2026-11-13-mstr-metadata-schema-json-poc.md
  - inbox/uni-semantic/2026-11-13-spotfire-information-link-xml-poc.md
  - inbox/pm/2026-11-13-dialect-transpiler-intent-pass.md
  - inbox/pm/2026-11-13-unresolved-expression-intent-pass.md
  - inbox/pm/2026-11-13-mstr-metadata-schema-json-intent-pass.md
  - inbox/pm/2026-11-13-pm-checkpoint-spotfire-il-intent-pass.md
  - ticket:fc04b030-4fbf-4c32-a73c-d94fc5597cbb
  - ticket:adeab157-a8f1-4d16-bd8f-ea0c9a8de05d
  - ticket:385b033c-0998-45fa-8b8a-8012d50f9989
  - ticket:8c7085b8-d1ab-49b7-8b88-c2b375aafcfa
  - ticket:0c9cee5a-858a-4f3d-bae3-7cb928a56d6a
tags: ["Engineering", "uni-semantic", "Phase3", "Dialect", "Spoke"]
type: wiki
---

# uni-semantic Phase 3: Dialect Transpiler · Unresolved · MSTR · Spotfire

Parent milestone `fc04b030` — ROADMAP Phase 3 all `[x]` after Unresolved Intent pass (2026-11-13). `tenant_cd` N/A → Done = merge + local `cargo test` 증거.

## Dialect Transpiler

- Crate `transpiler/` (`dialect_transpiler`).
- **Classifier:** `(dialect, expression)` → `intersection`(`sum`|`count`|`avg`) | `difference`. Common aggs = ARCHITECTURE §1.4 only (LookML `type:average` → avg).
- Difference markers: DAX `CALCULATE`/`FILTER`/…, LOD `{FIXED|INCLUDE|EXCLUDE}`, MSTR `{#…}`/`{~+}`, LookML non-sum/count/average `type:`.
- **Compile:** `compile`/`compile_all` — intersection → IR-canonical `sum|count|avg(operand)`; difference → existing `$defs/unresolved_expression` (`dialect`+`expression`+`warning`). No `$defs` extension.
- LookML `type:sum` 등 operand 없는 교집합은 aggregation만, `ir_expression=None`.
- PR #14 classifier `3a4a3c39…`; PR #15 unresolved `3e0132ac`. Verify: `cargo test -p dialect_transpiler`.

## MSTR Modeling REST Schema JSON

- Spoke `frontends/mstr` (`frontend_mstr`). Synthetic Schema JSON SoR (`tables[]`/`relationships[]`); live HTTP·시크릿 Non-goals.
- Map: `physicalTable.columns` → IR `table`; `tableKey`+ID form `expression.text` → `pk`; relationship → `fk`/`viewJoin`. `$defs` additive 없음.
- PR #13. Verify: `cargo test -p frontend_mstr`.

## Spotfire Information Link XML

- Spoke `frontends/spotfire`. Vendor IL/Library export 재배포 불가 → 합성 `informationLink` fixture.
- Min tags: `columns/column`(@schema/@table/@column/@dataType/@key) + `joins/join` equi. Non-goals: DXP embed · Library zip · Filter/Procedure.
- PR #12 `67e6f704…`. Verify: `cargo test -p frontend_spotfire`.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Phase2-Spokes.md]]
- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md]]
- [[wiki/Engineering/Data-and-Security/OSI-Open-Semantic-Interchange.md]]
