---
id: inbox-ta-unitutor-pages-custom-domain-api
agent: ta
ticket_id: 25217dd4-521b-452e-ba9f-e4766b3898af
updated: 2026-10-02
status: inbox
sources:
  - ticket:25217dd4-521b-452e-ba9f-e4766b3898af
  - https://developers.cloudflare.com/api/resources/pages/subresources/projects/subresources/domains/methods/create/
  - https://github.com/yoosungung/UniTutorAI/pull/18
---

# UniTutor Pages custom domain via API (not wrangler)

- `wrangler pages` has no domain add/list CLI; attach with Cloudflare API `POST /accounts/{id}/pages/projects/{project}/domains` body `{"name":"tutor.askwho.net"}`.
- After Pages assets are live (`*.pages.dev` 200), custom host stays NXDOMAIN until domain attach; same-account zone usually creates DNS/TLS.
- CI pattern: idempotent list+POST after `deploy:pages`, then longer curl retries for first smoke on custom host.
