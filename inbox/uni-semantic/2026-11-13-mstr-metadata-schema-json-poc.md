---
id: inbox-uni-semantic-mstr-metadata-schema-json-poc
agent: uni-semantic
ticket_id: 8c7085b8-d1ab-49b7-8b88-c2b375aafcfa
updated: 2026-11-13
status: inbox
sources:
  - ticket:8c7085b8-d1ab-49b7-8b88-c2b375aafcfa
  - https://github.com/yoosungung/uni-semantic/pull/13
---

# MSTR Modeling REST Schema JSON → IR (PoC)

- Spoke: `frontends/mstr` — 합성 fixture SoR (`tables`/`attributes`/`relationships`); 실테넌트 HTTP·시크릿 Non-goals.
- IR: physical table(+`tableKey`→pk, relationship→fk) · join `view`; `$defs` additive 없음.
- Attribute ID form `expression.text`만 컬럼 식별 (tokens/tree는 Risks).
- Verify: `cargo test -p frontend_mstr` (2 passed).
