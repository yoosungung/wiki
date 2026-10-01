---
id: inbox-ta-unitutor-tutor-askwho-domain
agent: ta
ticket_id: f7f980f3-ac59-42fc-a462-45ecfe6df2b8
updated: 2026-10-01
status: inbox
sources:
  - ticket:f7f980f3-ac59-42fc-a462-45ecfe6df2b8
  - https://github.com/yoosungung/UniTutorAI/pull/9
---

# UniTutor tutor.askwho.net domain prep

- Prod hosts: Pages `tutor.askwho.net`, Worker `api.tutor.askwho.net` (custom_domain in `backend/wrangler.jsonc`).
- Eric typed `tutor.askwhow.net`; TA assumed `askwho.net` zone (same as factory).
- Remote deploy still needs `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID`; Pages custom domain attach after first Pages project exists.
- Pattern mirrors factory `deploy/SETUP.md` custom domain section.
