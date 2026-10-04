---
id: inbox-uni-tutor-on-device-webllm
agent: uni-tutor
ticket_id: e54e2e1b-9459-4da1-ab02-a239af24af6c
updated: 2026-10-04
status: inbox
sources:
  - ticket:e54e2e1b-9459-4da1-ab02-a239af24af6c
  - wiki/Models/Optimization-and-Serving/WebLLM-Engine.md
  - wiki/Engineering/Development-Environment/WebGPU-및-WebNN-표준화-현황-2026.md
  - https://www.npmjs.com/package/@mlc-ai/web-llm
---

# UniTutor 온디바이스 WebLLM 슬라이스

- TutorTurn 라우팅(opt-in): on-device WebLLM → (불가 시 `on_device_unsupported`/`on_device_failed`, 클라우드 무전환) / 오프면 SSE(+BYOK→앱 Gemini).
- `@mlc-ai/web-llm` 0.2.85는 동적 로드 + worker; 기본 클라우드 경로에 상주하지 않음.
- WebGPU 없으면 명시적 unsupported. COOP/COEP·대용량 첫 다운로드 UX는 후속(YouTube iframe 충돌 위험).
- 온디바이스 활성 시 무료 문답 한도 미과금(클라우드 추론 $0) — BYOK와 동일 취급.
- ROADMAP을 crewrp식 `##`+checkbox로 맞춤: 1–3단계 `[x]`, 4단계 on-device `[ ]`, 「나중」은 비체크리스트 카탈로그.
