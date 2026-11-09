---
id: inbox-candidate-option-a-report-api
agent: candidate
ticket_id: f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
updated: 2026-11-09
status: inbox
sources:
  - ticket:f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
  - https://github.com/berryking404/candidate.win/pull/24
---

# candidate.win Option A — /api/report Worker

- Hugo/GitHub Pages alone cannot hold `CANDYDATE_ISSUES_TOKEN` at runtime; baking into static build would leak it.
- `wiki.candidate.win` is already behind Cloudflare → same-origin `POST /api/report` Worker (`edge/report`) creates Issues with the secret.
- Browser modal uses `CandydateReport.buildReportPayload` + `submitReport` only; no `window.open` to github.com; user-facing errors are generic retry messages.
- Internal SoR remains GitHub Issues; public README/ROADMAP/CoC describe site form UX, not GitHub login.
- Deploy: `wrangler secret put CANDYDATE_ISSUES_TOKEN` + route `wiki.candidate.win/api/report*`.
