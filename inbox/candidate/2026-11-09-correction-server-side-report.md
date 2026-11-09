---
id: inbox-candidate-correction-server-side-report
agent: candidate
ticket_id: f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
updated: 2026-11-09
status: inbox
sources:
  - ticket:f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
  - ticket:59ff5fda-f1a8-4ea2-ad76-17307e603b66
  - https://github.com/berryking404/candidate.win/pull/24
---

# candidate.win 정정·삭제 Option A (서버측 Issues)

- Hugo/GitHub Pages는 런타임 시크릿 불가 → Cloudflare Worker `POST /api/report` (`edge/report`)가 `CANDYDATE_ISSUES_TOKEN`으로 Issues 생성.
- 웹 모달은 `fetch('/api/report')`만; `window.open`·github.com·로그인 유도 제거 (AGENTS.md Repository Contract).
- 내부 SoR=Issues, UX=사이트 폼. ROADMAP/README/CODE_OF_CONDUCT/status 문구 정렬.
- prod 스모크 전: wrangler secret + `wiki.candidate.win/api/report*` 라우트 연결 필요.
