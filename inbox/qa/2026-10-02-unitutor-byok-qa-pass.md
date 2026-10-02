---
id: inbox-qa-unitutor-byok-qa-pass
agent: qa
ticket_id: 5845c0fd-e3e9-4427-b41d-dca12f9de7b5
updated: 2026-10-02
status: inbox
sources:
  - ticket:5845c0fd-e3e9-4427-b41d-dca12f9de7b5
  - https://github.com/yoosungung/UniTutorAI/pull/16
  - https://unitutor.pages.dev
  - https://api.tutor.askwho.net/health
---

# UniTutor BYOK QA pass (vitest smoke + remote probe)

- Tenant has no Playwright; AC1/AC2 covered by `byok.smoke`/`byok`/`tutorStream` + backend BYOK header tests (all green on merge `2ea04f7`).
- Deployed SPA `unitutor.pages.dev` ships ByokPanel strings + `X-UniTutor-Byok-Key`; custom domain `tutor.askwho.net` DNS unresolved at QA time.
- Remote Worker accepts BYOK header (CORS allow + SSE path); fake key → `llm_failed` without key echo. Live Gemini completion not proven (env fails for both BYOK and non-BYOK).
