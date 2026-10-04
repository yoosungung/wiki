---
id: unitutor-on-device-webllm
title: "UniTutor on-device WebLLM TutorTurn opt-in"
status: canonical
owner: km
updated: "2026-10-05"
review_after: "2027-01-05"
sources:
  - inbox/uni-tutor/2026-10-04-unitutor-on-device-webllm.md
  - ticket:e54e2e1b-9459-4da1-ab02-a239af24af6c
  - wiki/Models/Optimization-and-Serving/WebLLM-Engine.md
  - wiki/Engineering/Development-Environment/WebGPU-및-WebNN-표준화-현황-2026.md
  - https://www.npmjs.com/package/@mlc-ai/web-llm
tags: ["Engineering", "AI-Native", "UniTutor", "WebLLM", "On-Device"]
type: "wiki"
---

# UniTutor on-device WebLLM TutorTurn opt-in

## Routing

- Opt-in path: on-device WebLLM → on failure emit `on_device_unsupported` / `on_device_failed` (**no silent cloud fallback**). Off → SSE (+ BYOK → app Gemini).
- `@mlc-ai/web-llm` **0.2.85** dynamic load + worker; not resident on default cloud path.
- No WebGPU → explicit unsupported. COOP/COEP and large first-download UX are follow-ups (YouTube iframe conflict risk).
- When on-device active: free Q&A quota not charged (cloud $0) — same treatment as BYOK.

## Roadmap shape

- Align ROADMAP to crewrp-style `##`+checkbox: stages 1–3 `[x]`, stage 4 on-device `[ ]`; 「나중」 is non-checklist catalog.

## Related

- [[wiki/Models/Optimization-and-Serving/WebLLM-Engine.md]]
- [[wiki/Engineering/AI-Native-Engineering/UniTutor-TutorTurn-SSE-Inference.md]]
- [[wiki/Engineering/AI-Native-Engineering/UniTutor-BYOK-Browser-Oneshot.md]]
