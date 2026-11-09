---
id: inbox-candidate-option-a-report-api
agent: candidate
ticket_id: f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
updated: 2026-11-09
status: inbox
sources:
  - ticket:f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
  - ticket:dab8e0cf-335e-4ef3-baab-8a44fb9c3ef0
  - https://github.com/berryking404/candidate.win/pull/24
---

# candidate.win Option A: 정정·삭제 서버측 Issues

- Eric 승인 Option A: Repository Contract(GitHub 비노출) 유지 + 서버/엣지에서 Issues 생성.
- Hugo/GitHub Pages는 런타임 시크릿 불가 → Cloudflare Worker `edge/report`가 `POST /api/report` 처리, `CANDYDATE_ISSUES_TOKEN`은 Worker 시크릿.
- 브라우저: `CandydateReport.buildReportPayload` + `fetch('/api/report')` only; `window.open`·github.com UX 제거.
- 배포 후 라우트 `wiki.candidate.win/api/report*` 를 Worker에 연결해야 스모크 가능.
