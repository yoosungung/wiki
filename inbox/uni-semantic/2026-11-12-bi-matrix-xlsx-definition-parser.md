---
id: inbox-uni-semantic-bi-matrix-xlsx-definition-parser
agent: uni-semantic
ticket_id: c0279283-7f5e-4c55-b347-5778cb48e1b2
updated: 2026-11-12
status: inbox
sources:
  - ticket:c0279283-7f5e-4c55-b347-5778cb48e1b2
  - https://github.com/yoosungung/uni-semantic/pull/9
  - https://audp.bimatrix.co.kr/download/attachments/79408392/%5BAUD%ED%94%8C%EB%9E%AB%ED%8F%BC%5D%20i-MATRIX%20Designer%20%EA%B0%9C%EB%B0%9C%EC%9E%90%20%EB%A7%A4%EB%89%B4%EC%96%BC.pdf?api=v2&modificationDate=1731478729262&version=1
---

# uni-semantic: BI Matrix 테이블정의서 `.xlsx` → IR

- SoR 시트명 `테이블정의서`; 헤더 `Table`/`Table 설명`/`Owner`/`순서`/`항목명`/`Type`/`Null 허용`/`Key`/`비고` (i-MATRIX Designer [테이블 정의서]).
- Type: 문자형→varchar · 숫자형→numeric · 날짜형→date; Key 숫자/`PK` → `table.pk`; FK 없음 → `fk=[]`.
- 구현: Rust + `calamine` (`frontends/bi_matrix`); Python 사이드카 불필요(thin 템플릿). 검증 `cargo test -p frontend_bi_matrix`.
- V1/D1/P1 보고서·i-META 비범위.
