---
id: inbox-pm-unitutor-byok-inference-routing-intake
agent: pm
ticket_id: 75a80417-a6a3-4585-97d1-35ad8ef6b7db
updated: 2026-10-02
status: inbox
sources:
  - ticket:75a80417-a6a3-4585-97d1-35ad8ef6b7db
  - ticket:b38f6234-cdfb-4350-92e9-cf84d25023f8
  - https://github.com/yoosungung/UniTutorAI/blob/main/AGENTS.md
  - https://github.com/yoosungung/UniTutorAI/blob/main/backend/DESIGN.md
---

# UniTutor — Stage3 done → BYOK·추론 라우팅 intake

- 1–3단계 factory 티켓 전부 done. AGENTS Status 다음 문장 SoR: **BYOK·추론 라우팅**.
- backend는 `/health`만; FE는 `mockTutorTurn`. DESIGN§2.1 SSE+Gemini cascade는 미구현.
- 자식: `b38f6234` SSE 라우팅 in_progress @uni-tutor; `5845c0fd` BYOK는 ROADMAP 미결정 → eric approval; `25217dd4` 첫 원격 deploy는 Actions secrets 게이트(DNS 미해석).
- BYOK는 라우팅 Intent 후 kickoff; 키 보관 기본안은 브라우저 only + one-shot.
