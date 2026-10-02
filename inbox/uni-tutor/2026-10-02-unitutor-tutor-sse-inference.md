---
id: inbox-uni-tutor-tutor-sse-inference
agent: uni-tutor
ticket_id: b38f6234-cdfb-4350-92e9-cf84d25023f8
updated: 2026-10-02
status: inbox
sources:
  - ticket:b38f6234-cdfb-4350-92e9-cf84d25023f8
  - ticket:75a80417-a6a3-4585-97d1-35ad8ef6b7db
---

# UniTutor TutorTurn SSE 추론 라우팅

- Workers `POST /api/tutor/turn` → SSE `tutor_turn_delta` / `tutor_turn` / `error` (ARCHITECTURE §2.6).
- MVP Provider: Gemini `streamGenerateContent?alt=sse` via `services/llm.ts`. 키 없으면 503 `llm_unavailable`(키 미노출).
- FE: `lib/tutorStream.ts` + `hooks/useTutorTurn.ts`; mock은 테스트 픽스처·DEV 폴백만.
- BYOK·DeepSeek cascade·KV 캐시는 Non-goal / 후순위.
