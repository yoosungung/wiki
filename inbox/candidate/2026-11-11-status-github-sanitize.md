---
id: inbox-candidate-status-github-sanitize
agent: candidate
ticket_id: 2da67ba7-7f33-47ac-bf27-af5cd90f5897
updated: 2026-11-11
status: inbox
sources:
  - ticket:2da67ba7-7f33-47ac-bf27-af5cd90f5897
  - wiki/Engineering/AI-Native-Engineering/Candidate-Correction-Report-Worker.md
  - https://wiki.candidate.win/status/
  - https://github.com/berryking404/candidate.win/pull/35
---

# candidate.win `/status/` GitHub sanitize

- 공개 `/status/`는 `fetch_issues.py` → `reports.json` 경로에서 `sanitize_public_status_text`로 `github.com`·`GitHub`·`factory.askwho.net` URL을 제거한 뒤 빌드한다.
- Hugo `status.html`은 `replaceRE` 렌더 가드로 동일 패턴을 markdownify 직전에 한 번 더 제거한다(fetch 누락 방어).
- 공개 카피(`status.md`/`policy.md`)는 `Closes #N`·「저장소」 대신 현황 페이지 공개 문구로 교체.
- 공개 답변 작성 규칙: Actions/PR URL·SHA·ticket id는 factory 코멘트에만; 공개는 「요청하신 … 반영」 패턴 (`AGENTS.md`).
- Option A 모달(`/api/report`)은 기존처럼 `window.open`/github.com 비노출 유지(회귀 테스트 포함).
