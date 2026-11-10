---
id: inbox-candidate-2026-11-10-report-worker-gh-actions-cd
agent: candidate
ticket_id: f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
updated: 2026-11-10
status: inbox
sources:
  - ticket:f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
  - wiki/Engineering/AI-Native-Engineering/Candidate-Correction-Report-Worker.md
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
  - https://github.com/berryking404/candidate.win/pull/25
---

# candidate.win report Worker: GH Actions CD

- Closeout path is Actions (`deploy-report-worker.yml`), not local wrangler — Eric preference 2026-11-10.
- `wrangler.toml` declares `[[routes]]` `wiki.candidate.win/api/report*` + `zone_name = candidate.win` (CD-owned route, not dashboard one-shot).
- Required Actions secrets: `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`, existing `CANDYDATE_ISSUES_TOKEN` (CI injects Worker secret).
- Live smoke still needs secrets present + merge/`workflow_dispatch`; until then `/api/report` may stay 405.
