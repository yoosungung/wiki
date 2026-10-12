---
id: inbox-qa-unitutor-path-chrome-qa-smoke
agent: qa
ticket_id: 793c7592-3071-4ab1-a07b-f96a9ee8703c
updated: 2026-10-12
status: inbox
sources:
  - ticket:793c7592-3071-4ab1-a07b-f96a9ee8703c
  - https://github.com/yoosungung/UniTutorAI/pull/32
  - https://unitutor.askwho.net/
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
  - inbox/uni-tutor/2026-10-12-path-chrome-gating-strip.md
---

# UniTutor PathChrome — QA browser smoke

- Live: `unitutor.askwho.net` bundle `index-CNUNvGqh.js` contains PathChrome a11y (`학습 경로`, `aria-expanded`).
- Playwright (mobile 390×844): onboarding → 경로 만들기 → default collapsed (`aria-expanded=false`, no PathView) → expand → PathView + 막힘 → detour badge「우회」while collapsed → re-expand detour placement + 우회 끝 → keyboard Enter expands.
- Collapsed chrome height ~53px / 844vh ≈ 0.063 (AC2 viewport).
- merge_sha: `73178e81677b9c9c81ff72440e2196a06680d848` (main HEAD).
