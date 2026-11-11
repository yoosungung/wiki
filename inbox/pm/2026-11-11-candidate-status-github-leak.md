---
id: inbox-pm-candidate-status-github-leak
agent: pm
ticket_id: 2da67ba7-7f33-47ac-bf27-af5cd90f5897
updated: 2026-11-11
status: inbox
sources:
  - ticket:2da67ba7-7f33-47ac-bf27-af5cd90f5897
  - wiki/Engineering/AI-Native-Engineering/Candidate-Correction-Report-Worker.md
  - https://wiki.candidate.win/status/
---

# candidate.win `/status/` GitHub 누수

- Option A(`/api/report`) 모달 경로는 GitHub 비노출 유지.
- 공개 `/status/` 답변 본문에 agent closeout의 `github.com/.../actions/runs/...` URL이 렌더됨 (계약 위반).
- `wiki/content/status.md` 공개 원칙에 `Closes #N`·「저장소」 용어 잔존.
- 가드 우선순위: **공개 렌더 sanitize 필수**, Issue 댓글 작성 규칙은 보조.
