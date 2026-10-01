---
id: inbox-pm-unitutor-tutor-askwho-domain-intent
agent: pm
ticket_id: f7f980f3-ac59-42fc-a462-45ecfe6df2b8
updated: 2026-10-01
status: inbox
sources:
  - ticket:f7f980f3-ac59-42fc-a462-45ecfe6df2b8
  - https://github.com/yoosungung/UniTutorAI/pull/9
---

# UniTutor tutor.askwho.net domain Intent

- Eric `tutor.askwhow.net` → 관례상 `tutor.askwho.net` / API `api.tutor.askwho.net` (오타 가정).
- PR #9: Worker `custom_domain` route + SETUP DNS 충돌·verify curl + FE prod `VITE_API_BASE_URL` 예시. Merged `b41cc033`.
- 원격 배포는 여전히 `CLOUDFLARE_API_TOKEN` / `CLOUDFLARE_ACCOUNT_ID` 게이트.
