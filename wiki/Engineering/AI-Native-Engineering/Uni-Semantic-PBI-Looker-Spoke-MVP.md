---
id: uni-semantic-pbi-looker-spoke-mvp
title: "uni-semantic: Power BI ↔ Looker spoke MVP"
status: canonical
owner: km
updated: "2026-11-12"
last_updated: "2026-11-12"
review_after: "2027-02-12"
sources:
  - inbox/uni-semantic/2026-11-11-pbi-looker-spoke-mvp.md
  - inbox/pm/2026-11-11-uni-semantic-pbi-looker-spoke-intake.md
  - ticket:4698bcf5-9aff-46b0-93d4-c2ed3ce01cd1
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
tags: ["Engineering", "uni-semantic", "PowerBI", "Looker"]
type: wiki
---

# uni-semantic: Power BI ↔ Looker spoke MVP

Hub-only: PBI→IR→Looker / Looker→IR→PBI. 선행 IR schema(`ir/`) done 후 스포크 I/O.

## 범위

| 축 | MVP | Non-goal |
| :--- | :--- | :--- |
| PBI 입력 | 단독 BIM JSON 서브셋 (tables/columns/relationships/simple SUM·COUNT·AVERAGE) | PBIP·전체 TMDL |
| LookML | view + explore + join + measure(sum/count/average) | 전체 Looker IDE |
| Cargo | `frontends|backends/{powerbi,looker}` + `ir/rust` serde 헬퍼 | Hub 우회 |

검증: `cargo test` (unit + `mvp_roundtrip` 양방향).

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md]]
- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-SQL-Parity-Normalize.md]]
