---
id: inbox-uni-semantic-sap-bo-unx-poc
agent: uni-semantic
ticket_id: e88e5771-ae0e-4afd-8b82-e224f6d94fab
updated: 2026-11-12
status: inbox
sources:
  - ticket:e88e5771-ae0e-4afd-8b82-e224f6d94fab
  - https://bobj-board.org/t/document-a-universe-unx/207869
  - https://gist.github.com/kfeoktistoff/5b3aa19f1aa1feb0607d
---

# SAP BO `.unx` PoC 추출 메모

- `.unx`는 zip 컨테이너; 내부 `.dfx`/`.blx`도 zip이며 그 안 XML이 Data Foundation·Business Layer.
- 공개 벤더 `.unx` 재배포 불가 → 합성 최소 fixture + DESIGN 태그 계약이 PoC SoR.
- BL `businessItems` `xsi:type` = Folder|Dimension|Measure (공개 gist 관측); PoC는 Measure SUM/COUNT/AVG + binding만 IR `metric`.
- Digest/해시·Contexts·Prompts·OLAP은 Non-goal; 실 IDT XML 변형은 adapter Risk.
