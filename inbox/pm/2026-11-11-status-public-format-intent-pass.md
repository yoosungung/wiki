---
id: inbox-pm-status-public-format-intent-pass
agent: pm
ticket_id: 2da67ba7-7f33-47ac-bf27-af5cd90f5897
updated: 2026-11-11
status: inbox
sources:
  - ticket:2da67ba7-7f33-47ac-bf27-af5cd90f5897
  - https://wiki.candidate.win/status/
  - https://github.com/berryking404/candidate.win/commit/8305e51b2a8e9aa6e9671bc17aef7df67fdf2a22
  - https://github.com/berryking404/candidate.win/actions/runs/42943530812
---

# candidate.win `/status/` 공개 포맷 재정렬 — intent pass

- main `8305e51b`: fetch 시 `format_public_request`/`format_public_reply` + URL sanitize 유지; AGENTS 공개 포맷 계약
- live `/status/`: `**페이지**`/`**내용**` + 「요청하신 …」; GH form/`Closed after factory`/`Resolved by PR`/`github.com` 0
- Issue #26/#27/#28 공개 답변 실수정 확인; Option A SoR 미변경
