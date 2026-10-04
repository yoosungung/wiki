---
id: inbox-qa-unitutor-picture-search-qa-pass
agent: qa
ticket_id: d4a9f487-7325-4ecc-b9b4-3dee165a425b
updated: 2026-10-04
status: inbox
sources:
  - ticket:d4a9f487-7325-4ecc-b9b4-3dee165a425b
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37164460300
  - https://unitutor.askwho.net/
  - https://api.tutor.askwho.net/health
---

# UniTutor PictureSearch QA smoke (Option A)

- Deploy run `37164460300` headSha `f39e3fe` (PR #26 merge) success + CI Smoke step.
- API: `GET https://api.tutor.askwho.net/health` → 200 `{"status":"ok","service":"unitutor-backend"}`.
- Pages: `https://unitutor.askwho.net/` 200.
- Browser smoke: onboarding「경로 만들기」→ PictureSearch `Functions` → iframe `start=341`.
- Note: Worker health path is `/health` (not `/api/health`); Pages `/api/health` returns SPA HTML.
