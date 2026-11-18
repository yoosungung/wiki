---
id: inbox-aura-agent-inject-contract
agent: aura
ticket_id: e9ef0dd8-658f-4fbc-80b1-a73f8be8fa13
updated: 2026-11-19
status: inbox
sources:
  - ticket:e9ef0dd8-658f-4fbc-80b1-a73f8be8fa13
  - https://github.com/yoosungung/aura/pull/29
---

# Aura Agent 주입 계약 (M2)

- Agent 메모리 컨텍스트 유일 소스 = `aura.rpc.memory.recall` 응답 `items[]`.
- 원문/`content_ref` 우회 덤프 금지 (ARCHITECTURE §1 #9).
- 슬롯 토큰: 합 2048 · short_term 512 · episodic 768 · long_term+semantic 768; 아이템 short 4 · top_k 12.
- 패킹 구현은 M3 `agent_invoke`; 정적 게이트 `check-agent-inject-contract.sh`.
