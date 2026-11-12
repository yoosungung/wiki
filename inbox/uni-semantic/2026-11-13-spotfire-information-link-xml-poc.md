---
id: inbox-uni-semantic-spotfire-il-xml-poc
agent: uni-semantic
ticket_id: 0c9cee5a-858a-4f3d-bae3-7cb928a56d6a
updated: 2026-11-13
status: inbox
sources:
  - ticket:0c9cee5a-858a-4f3d-bae3-7cb928a56d6a
  - https://docs.tibco.com/pub/sfire-analyst/latest/doc/html/en-US/TIB_sfire_client/client/topics/en-US/id_information_link_tab.html
  - https://community.spotfire.com/forums/topic/18885-postgresql-spotfire-information-model-migration-issues-due-to-case-sensitive-column-names/
---

# Spotfire Information Link XML PoC 계약

- 공개 벤더 IL/Library export XML 재배포 불가 → 합성 `informationLink` 루트 fixture로 PoC (Tableau/SAP BO와 동일 패턴).
- 최소 태그: `columns/column`(@schema/@table/@column/@dataType/@key) + `joins/join` equi left/right.
- DXP 임베드·Library zip·Filter/Procedure는 Non-goals. 실 export는 네임스페이스·GUID 참조 변형 Risk.
