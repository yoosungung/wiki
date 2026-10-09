---
id: inbox-pm-crewrp-pc-web-plan-review
agent: pm
ticket_id: 60f912ca-8f07-4115-a7b1-b911c9a6b84e
updated: 2026-10-09
status: inbox
sources:
  - ticket:60f912ca-8f07-4115-a7b1-b911c9a6b84e
  - ticket:f9f2416a-dc9c-4fed-8aaf-cfa25022c7c2
  - https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps
---

# CrewRP PC Web plan review

- CrewRP SoR clients = iOS/Android only; no Phase 4 / PC web in ROADMAP after Phase 3 freeze (pass-gate chose maintenance-only).
- PC web blocked until OAuth: auth-bridge `ALLOWED_REDIRECT_URIS` and GitHub OAuth App are `crewrp://oauth/callback` only — need HTTPS callback + CORS or BFF; avoid localStorage for tokens (PKCE S256; prefer memory/HttpOnly).
- Options for Eric: A full 4-tab parity SPA · B read-heavy thin · C auth spike then redecide (PM recommend) · D stay frozen.
- Ticket `60f912ca` → waiting_for_approval + assignee eric; `plan.md` attached.
