---
id: inbox-pm-uni-semantic-bi-matrix-xlsx-intent-pass
agent: pm
ticket_id: c0279283-7f5e-4c55-b347-5778cb48e1b2
updated: 2026-11-12
status: inbox
sources:
  - ticket:c0279283-7f5e-4c55-b347-5778cb48e1b2
  - https://github.com/yoosungung/uni-semantic/pull/9
---

# uni-semantic BI Matrix `.xlsx` → IR Intent pass

- Spoke `frontends/bi_matrix` (`frontend_bi_matrix`): i-MATRIX `테이블정의서` sheet → IR `table` (`pk` from Key, `fk=[]`).
- Stack: Rust + `calamine`; no Python sidecar for this thin template.
- Evidence: PR #9 merged `4eddde39`; `cargo test -p frontend_bi_matrix` 2 ok; workspace `cargo test` green.
- Closeout: library spoke → qa/aa/prod N/A; ticket done after Intent pass.
