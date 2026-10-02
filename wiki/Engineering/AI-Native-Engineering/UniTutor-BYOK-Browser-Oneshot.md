---
id: unitutor-byok-browser-oneshot
title: "UniTutor BYOK: browser custody + one-shot header"
status: canonical
owner: km
updated: "2026-10-03"
review_after: "2027-01-03"
sources:
  - inbox/pm/2026-10-02-byok-product-lock.md
  - inbox/pm/2026-10-02-unitutor-byok-inference-routing-intake.md
  - inbox/uni-tutor/2026-10-02-unitutor-byok-browser-oneshot.md
  - inbox/aa/2026-10-02-unitutor-byok-security-pass.md
  - inbox/qa/2026-10-02-unitutor-byok-qa-pass.md
  - ticket:5845c0fd-e3e9-4427-b41d-dca12f9de7b5
  - https://github.com/yoosungung/UniTutorAI/pull/16
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
tags: ["Engineering", "AI-Native", "UniTutor", "BYOK", "Security"]
type: "wiki"
---

# UniTutor BYOK: browser custody + one-shot header

## Product lock

- Eric 승인: BYOK **지금** 노출 (유료 루프 후 미룸 아님). 마커 `<!-- byok:approved -->`.
- 키 보관: **브라우저 only** (`localStorage` `unitutor:byok-gemini`). 서버 DB/KV 영속 금지.
- 전달: `POST /api/tutor/turn` 헤더 `X-UniTutor-Byok-Key` one-shot. BYOK 있으면 앱 `GEMINI_API_KEY`보다 우선·미사용.
- BYOK 활성 시 무료 일일 쿼ota 미과금(앱 추론 원가 $0).

## Security / QA

- 응답·SSE error에 키 미포함; CORS `allowHeaders`에 헤더명 명시.
- UniTutor에 `.factory/quality.yaml` `security.command` 없음 → mechanical SAST skip; AA는 tip↔merge 범위 리뷰 ([[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]).
- Residual: XSS → localStorage 탈취 가능(브라우저 custody 고유).
- QA: vitest `byok`/`tutorStream` + remote Worker fake-key → `llm_failed` without echo. Live Gemini 완결은 env 의존.

## Sequencing

Stage1–3 done 후 SoR 다음 문장 = BYOK·추론 라우팅. SSE 라우팅 Intent 뒤 BYOK kickoff.
