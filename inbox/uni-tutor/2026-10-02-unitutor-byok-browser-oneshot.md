---
id: inbox-uni-tutor-byok-browser-oneshot
agent: uni-tutor
ticket_id: 5845c0fd-e3e9-4427-b41d-dca12f9de7b5
updated: 2026-10-02
status: inbox
sources:
  - ticket:5845c0fd-e3e9-4427-b41d-dca12f9de7b5
  - ticket:ARCHITECTURE UniTutor §2.6
---

# UniTutor BYOK — browser custody + one-shot header

- Product lock: BYOK **지금** 노출; 키는 **브라우저 only** (`localStorage` `unitutor:byok-gemini`); 서버 DB/KV 영속 저장 금지.
- 전달: `POST /api/tutor/turn` 요청 헤더 `X-UniTutor-Byok-Key` one-shot. BYOK가 있으면 앱 `GEMINI_API_KEY`보다 우선·미사용.
- 보안: 응답·SSE error에 키 미포함; CORS `allowHeaders`에 헤더명 명시.
- 쿼ota: BYOK 활성 시 무료 일일 한도 미과금(앱 추론 원가 $0).
