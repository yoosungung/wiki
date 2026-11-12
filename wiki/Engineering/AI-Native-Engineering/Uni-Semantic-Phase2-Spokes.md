---
id: uni-semantic-phase2-spokes
title: "uni-semantic Phase 2: Tableau·BI Matrix·SAP BO·IR snowflake/Hierarchy"
status: canonical
owner: km
updated: "2026-11-13"
last_updated: "2026-11-13"
review_after: "2027-02-13"
sources:
  - inbox/uni-semantic/2026-11-12-tableau-tds-spoke.md
  - inbox/uni-semantic/2026-11-12-tableau-tds-classic-relation-parser.md
  - inbox/uni-semantic/2026-11-12-bi-matrix-xlsx-spoke.md
  - inbox/uni-semantic/2026-11-12-bi-matrix-xlsx-definition-parser.md
  - inbox/uni-semantic/2026-11-12-sap-bo-unx-poc.md
  - inbox/uni-semantic/2026-11-12-ir-snowflake-hierarchy.md
  - inbox/pm/2026-11-12-uni-semantic-tableau-tds-intent-pass.md
  - inbox/pm/2026-11-12-uni-semantic-bi-matrix-xlsx-intent-pass.md
  - inbox/pm/2026-11-12-uni-semantic-sap-bo-unx-intent-pass.md
  - inbox/pm/2026-11-12-uni-semantic-ir-snowflake-hierarchy-intent-pass.md
  - inbox/pm/2026-11-12-pm-checkpoint-uni-semantic-phase2-closeout.md
  - ticket:9c068a99-a7e9-437c-b93f-06590ba84e47
  - ticket:1cda6737-3e9e-4b7e-9a72-0d2df68ed82a
  - ticket:c0279283-7f5e-4c55-b347-5778cb48e1b2
  - ticket:e88e5771-ae0e-4afd-8b82-e224f6d94fab
  - ticket:68f4207a-e514-48cb-9243-f5d77c83e652
tags: ["Engineering", "uni-semantic", "Phase2", "Spoke"]
type: wiki
---

# uni-semantic Phase 2: Tableau·BI Matrix·SAP BO·IR snowflake/Hierarchy

Parent milestone `9c068a99` — 자식 4건 Intent pass + ROADMAP Phase 2 all `[x]` → parent **done** (2026-11-12). library/CLI · `tenant_cd` N/A → qa/aa/prod N/A; merge + local test 증거로 Done.

## Spokes

| Spoke | Crate | Input → IR | PR / tip | Verify |
| :--- | :--- | :--- | :--- | :--- |
| Tableau classic `.tds` | `frontends/tableau` (`frontend_tableau`) | `connection > relation` → `table`(+`fk`) + join `view` | #8 `63cc2459…` | `cargo test -p frontend_tableau` |
| BI Matrix `.xlsx` | `frontends/bi_matrix` | 시트 `테이블정의서` → `table` (`pk` from Key, `fk=[]`) | #9 `4eddde39` | `cargo test -p frontend_bi_matrix` |
| SAP BO `.unx` PoC | `frontends/sap_bo` | nested-zip → `.dfx`/`.blx` → `table`(+`fk`) · `metric` SUM\|COUNT\|AVG | #10 `2f82e964` | `cargo test -p frontend_sap_bo` |
| IR snowflake·Hierarchy | `ir/` | `$defs.snowflake_path`; Hierarchy optional `description`; levels ≥2 unique | #11 `b7d8c2f` | `cd ir && npm test` |

## 계약 요약

- **Tableau:** standalone `.tds` only; Non-goals `.tdsx`/embedded, Object Model `relationships`, LOD, federated multi-connection. Mapping additive — no `$defs` change for this spoke.
- **BI Matrix:** Rust + `calamine` only (no Python sidecar). Headers SoR: Table · Table 설명 · Owner · 순서 · 항목명 · Type · Null 허용 · Key · 비고. Types 문자형/숫자형/날짜형.
- **SAP BO:** synthetic fixture SoR (vendor `.unx` redistribution blocked). PoC tag contract ≠ full IDT schema.
- **IR:** `viewJoin.snowflake_path` `$ref` (`minItems`1/`uniqueItems`); omit=direct join; empty array invalid. Hierarchy additive optional `description`.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md]]
- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Phase3-Dialect-and-Spokes.md]]
- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Factory-Onboard.md]]
