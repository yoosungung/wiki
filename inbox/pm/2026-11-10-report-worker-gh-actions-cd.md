---
id: inbox-pm-2026-11-10-report-worker-gh-actions-cd
agent: pm
ticket_id: f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
updated: 2026-11-10
status: inbox
sources:
  - ticket:f35f32d7-3eeb-4ed6-983a-353d6db5c0ee
  - wiki/Engineering/AI-Native-Engineering/Candidate-Correction-Report-Worker.md
  - wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md
---

# candidate.win report Worker: GH Actions CD (not local wrangler)

- Eric preference (2026-11-10): deploy Cloudflare Worker via GitHub Actions using repo secrets `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID` (UniTutor/factory pattern).
- Option A code already on main (PR #24 / `0c957763`); live `POST /api/report` still 405 until route+Worker deploy.
- Repo already has `CANDYDATE_ISSUES_TOKEN` Actions secret; `CLOUDFLARE_*` were missing at handoff.
- Closeout path: candidate adds deploy job for `edge/report`; Eric supplies CF secrets; smoke for `prod:`.
