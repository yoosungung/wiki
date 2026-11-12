---
id: inbox-uni-semantic-bi-matrix-xlsx-spoke
agent: uni-semantic
ticket_id: c0279283-7f5e-4c55-b347-5778cb48e1b2
updated: 2026-11-12
status: inbox
sources:
  - ticket:c0279283-7f5e-4c55-b347-5778cb48e1b2
  - https://github.com/yoosungung/uni-semantic/pull/9
---

# uni-semantic: BI Matrix `.xlsx` 테이블정의서 → IR

- Spoke `frontends/bi_matrix` (`frontend_bi_matrix`) parses i-MATRIX Designer sheet `테이블정의서` into IR `table` (`pk` from Key, `fk=[]`).
- Template SoR headers: Table · Table 설명 · Owner · 순서 · 항목명 · Type · Null 허용 · Key · 비고. Types 문자형/숫자형/날짜형.
- Rust + calamine only for this thin template (no Python sidecar). Verify: `cargo test -p frontend_bi_matrix`.
