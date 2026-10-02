---
id: unitutor-tutorturn-sse-inference
title: "UniTutor TutorTurn SSE 추론 라우팅"
status: canonical
owner: km
updated: "2026-10-03"
review_after: "2027-01-03"
sources:
  - inbox/uni-tutor/2026-10-02-unitutor-tutor-sse-inference.md
  - inbox/uni-tutor/2026-10-02-unitutor-tutor-turn-sse.md
  - inbox/pm/2026-10-02-unitutor-byok-inference-routing-intake.md
  - ticket:b38f6234-cdfb-4350-92e9-cf84d25023f8
  - ticket:75a80417-a6a3-4585-97d1-35ad8ef6b7db
tags: ["Engineering", "AI-Native", "UniTutor", "SSE"]
type: "wiki"
---

# UniTutor TutorTurn SSE 추론 라우팅

- Workers `POST /api/tutor/turn` → SSE `tutor_turn_delta` / `tutor_turn` / `error` (tenant ARCHITECTURE §2.6).
- MVP Provider: Gemini `streamGenerateContent?alt=sse` (`services/llm.ts`). 키 없으면 **503** `{ "error": "llm_unavailable" }` (키 미노출).
- FE: `lib/tutorStream.ts` + `hooks/useTutorTurn.ts`; mock은 테스트·DEV 폴백만.
- Non-goal(후순위): DeepSeek cascade·KV 캐시. BYOK는 별도 페이지 [[wiki/Engineering/AI-Native-Engineering/UniTutor-BYOK-Browser-Oneshot.md]].
