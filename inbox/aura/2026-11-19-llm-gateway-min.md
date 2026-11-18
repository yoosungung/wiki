---
id: inbox-aura-llm-gateway-min
agent: aura
ticket_id: b7910957-9c76-4d54-9478-f9363fec5b29
updated: 2026-11-19
status: inbox
sources:
  - ticket:b7910957-9c76-4d54-9478-f9363fec5b29
  - deploy/docs/llm-gateway.md
---

# Aura M3: LLM Gateway 최소 + Function Egress는 Gateway만

- §9.4 최소 경로: `services/llm-gateway` — `POST /v1/chat/completions`, tenant Token Bucket(20/s·burst40), circuit breaker, usage/cost 로그.
- Function 클라이언트(`client.js`)는 `aura-llm-gateway*`만 허용; `api.openai.com` 등 → `provider_direct_forbidden`.
- Deployment `aura-llm-gateway` replicas≥2 · label `app: aura-llm-gateway` (샌드박스 NP peer).
- 검증: `bash deploy/scripts/check-llm-gateway.sh` (클러스터·live provider 키 불필요).
- Non-goals: Fallback/과금 대시보드(M5) · live provider CI.
