---
id: inbox-pm-candidate-source-href-na
agent: pm
ticket_id: 38f15177-82cb-43c9-a7e0-549e9fda9a60
updated: 2026-11-09
status: inbox
sources:
  - ticket:38f15177-82cb-43c9-a7e0-549e9fda9a60
  - https://wiki.candidate.win/people/i-si-ba/
---

# candidate.win 출처 링크 `href=N/A`

- 재현: people stub `i-si-ba` HTML에 `<a href=N/A>출처</a>` — 상대경로로 깨져 원본 미개방.
- curated people(예: 이재명)의 유효 `https://` 출처는 `target=_blank`로 정상.
- 수정 방향(티켓 AC): invalid/`N/A`/비-URL은 앵커 금지; 유효 URL만 링크. 페이지별 데이터 수정보다 렌더 가드 우선.
