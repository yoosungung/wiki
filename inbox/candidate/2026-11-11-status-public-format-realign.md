---
id: inbox-candidate-status-public-format-realign
agent: candidate
ticket_id: 2da67ba7-7f33-47ac-bf27-af5cd90f5897
updated: 2026-11-11
status: inbox
sources:
  - ticket:2da67ba7-7f33-47ac-bf27-af5cd90f5897
  - https://wiki.candidate.win/status/
  - https://github.com/berryking404/candidate.win/issues/8
  - https://github.com/berryking404/candidate.win/issues/10
---

# candidate.win `/status/` 공개 포맷 재정렬

- 공개 정본: 요청 `**페이지**`/`**내용**`, 답변 「요청하신 … 반영했습니다」(Issue #8/#10).
- `format_public_request`가 Option A/GH form `###` 덤프를 공개 요약으로 변환(Issue 원문 SoR 유지).
- `format_public_reply`가 `Closed after factory`/`Resolved by PR` closeout을 사용자 문장으로 재작성(+ URL sanitize 유지).
- 최근 댓글 실수정: #26/#27/#28(+ live 노출 #23).
