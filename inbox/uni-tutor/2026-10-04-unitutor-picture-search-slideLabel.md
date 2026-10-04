---
id: inbox-uni-tutor-picture-search-slidelabel
agent: uni-tutor
ticket_id: d4a9f487-7325-4ecc-b9b4-3dee165a425b
updated: 2026-10-04
status: inbox
sources:
  - ticket:d4a9f487-7325-4ecc-b9b4-3dee165a425b
  - https://github.com/yoosungung/UniTutorAI/pull/26
---

# UniTutor PictureSearch (slideLabel/concept)

- Option A: 정적 `SourceSpan.slideLabel`/`concept` 부분 문자열 검색 → `CitationSelected` seek. 비전·임베딩 없음.
- 진입: `frontend/src/lib/pictureSearch.ts`, `components/canvas/PictureSearch.tsx`.
- PRODUCT §7: 이미지/비전 검색·Editor·Roommate는 여전히 나중 모드. ARCHITECTURE 스키마 변경 없음.
- 검증: `cd frontend && npm test` 110 passed (PR #26).
