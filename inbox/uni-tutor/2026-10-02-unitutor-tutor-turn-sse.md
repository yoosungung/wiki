---
id: inbox-uni-tutor-tutor-turn-sse
agent: uni-tutor
ticket_id: b38f6234-cdfb-4350-92e9-cf84d25023f8
updated: 2026-10-02
status: inbox
sources:
  - ticket:b38f6234-cdfb-4350-92e9-cf84d25023f8
  - repo:UniTutorAI ARCHITECTURE §2.6
---

# UniTutor TutorTurn SSE (Workers + Gemini)

- `POST /api/tutor/turn` → SSE events `tutor_turn_delta` / `tutor_turn` / `error` (ARCHITECTURE §2.6).
- Missing `GEMINI_API_KEY` → **503** `{ "error": "llm_unavailable" }` (no key leak).
- MVP Provider: Gemini only; KV cache / DeepSeek cascade deferred.
- FE: `lib/tutorStream.ts` + `hooks/useTutorTurn.ts`; DEV-only local template fallback.
