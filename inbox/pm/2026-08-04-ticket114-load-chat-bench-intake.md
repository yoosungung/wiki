---
id: inbox-pm-ticket114-load-chat-bench-intake
agent: pm
ticket_id: 114
updated: 2026-08-04
status: inbox
sources:
  - ticket:114
  - ticket:99
  - ticket:113
  - https://github.com/yoosungung/nl2sql/blob/main/load/smoke.py
  - https://github.com/yoosungung/nl2sql/blob/main/.factory/quality.yaml
  - https://github.com/yoosungung/sw-factory/blob/main/examples/tenant-quality/README.md
---

# nl2sql ta-load-weekly chat/bench intake (#114)

- #99는 health-only `load/smoke.py`를 `quality.yaml` `load.command`에 등록; Eric 요청으로 채팅 경로 벤치 강화(#114).
- PM Option A: 기존 httpx `load/` 확장(새 k6 의존성 없음). 시나리오 = health warm-up + `POST /api/chat`(SSE) + `GET /api/conversations`.
- 주간 기본 = in-process deterministic agent(SGLang/실 LLM OFF; `test_chat._FakeAgent` 정합). `LOAD_BASE_URL` + forwarded auth optional; `LOAD_REAL_LLM=1` opt-in.
- 임계 기본안: N≥20 · conc=5 · err=0 · in-process p95&lt;2s · wall≤10m. tenant_cd Done 증거 N/A(주간 NF).
- 구현 owner: nl2sql 서브태스크 #116. Review `@pm`.
