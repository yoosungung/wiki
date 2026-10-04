---
id: inbox-pm-unitutor-picture-search-intent-pass
agent: pm
ticket_id: d4a9f487-7325-4ecc-b9b4-3dee165a425b
updated: 2026-10-04
status: inbox
sources:
  - ticket:d4a9f487-7325-4ecc-b9b4-3dee165a425b
  - https://github.com/yoosungung/UniTutorAI/pull/26
---

# UniTutor PictureSearch Intent pass (Option A)

- 정적 `slideLabel`/`concept` 검색 UI → 기존 `CitationSelected`/`startSec` seek. 비전·임베딩·Editor·Roommate·ARCHITECTURE 스키마 확장 없음.
- PR #26 squash-merge `f39e3fe1f422d66e73fdc8e51c8b4836e751aefe`; CI backend+frontend green; `test:` frontend npm test 110 passed.
- 다음: tenant CD test (`@ta`) → qa/aa → prod 증거 후 done.
