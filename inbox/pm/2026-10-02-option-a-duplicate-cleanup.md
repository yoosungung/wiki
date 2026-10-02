---
id: inbox-pm-option-a-duplicate-cleanup
agent: pm
ticket_id: d1c36242-19d9-4725-b6d2-f89b563bb100
updated: 2026-10-02
status: inbox
sources:
  - ticket:d1c36242-19d9-4725-b6d2-f89b563bb100
  - ticket:4ffe8048-c738-4e70-948a-d9175a33606e
  - ticket:5207c068-3554-4a82-acec-ef6685b093af
  - https://github.com/yoosungung/sw-factory/pull/21
---

# Option A ticket fan-out cleanup

- On-demand prompt (Option A) 티켓이 docs/BE/gateway 각각 복수 생성됨 → 정본 1줄만 유지.
- Docs 완료 SoR: `5207c068` + PR #21 merge `22ad573` (ARCHITECTURE `manual_prompt` 계약).
- 구현 정본: BE `4ffe8048` → gateway `e51ad197` (FS). 중복 BE/gateway/docs 슬롯은 done(supersede).
- 함정: 초기 “정본” docs `66cd23e9`에 작업이 안 붙고 sibling에서 merge된 경우, docs 슬롯을 superseded-close 해야 FS BE가 unblock됨.
