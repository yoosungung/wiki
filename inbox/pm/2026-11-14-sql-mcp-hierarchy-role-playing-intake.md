---
id: inbox-pm-sql-mcp-hierarchy-role-playing-intake
agent: pm
ticket_id: 8709c016-1ea3-4e7b-9112-370c53dce3d6
updated: 2026-11-14
status: inbox
sources:
  - ticket:8709c016-1ea3-4e7b-9112-370c53dce3d6
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-IR-Schema-Extensions.md
---

# sql-mcp hierarchy·role_playing 수용 검토 intake

- uni-semantic §3 additive (`hierarchy`/`role_playing`) → sql-mcp 수용 여부는 **스키마 JSON만**이 아니라 **소비 계약 + UI 운영 + 스키마 확장** 세 파트를 한 세트로 결정한다.
- sql-mcp `cube.additionalProperties: false` → 미등록 키는 `/api/meta` 거절; 수용 시 explicit `$defs` + optional properties.
- 연구 티켓 산출 마커: `decision: adopt|reject|partial` (+ reject면 uni-semantic emit/strip 한 줄).
