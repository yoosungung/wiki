---
id: inbox-candidate-report-modal-done-closes
agent: candidate
ticket_id: 63833bbf-76a6-493d-854c-404c3ffb5488
updated: 2026-11-10
status: inbox
sources:
  - ticket:63833bbf-76a6-493d-854c-404c3ffb5488
  - wiki/Engineering/AI-Native-Engineering/Candidate-Correction-Report-Worker.md
---

# 정정·삭제 모달: 접수 완료 클릭 시 닫기

- `wiki/layouts/_default/baseof.html` `submitReport`: 성공 후 버튼 라벨 `접수 완료` + `disabled=false`; 재클릭 시 `closeReportModal()`.
- 이전엔 성공 후 버튼이 disabled라 사용자가 닫을 수 없었고 Escape/오버레이만 가능.
