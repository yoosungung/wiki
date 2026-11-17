---
id: inbox-aura-aura-dlq-term-path
agent: aura
ticket_id: 1632b9ee-7d25-4a9d-96f9-2a8cd83f72b4
updated: 2026-11-17
status: inbox
sources:
  - ticket:1632b9ee-7d25-4a9d-96f9-2a8cd83f72b4
  - https://github.com/yoosungung/aura/pull/8
---

# AURA_DLQ 적재 = ① Term (Advisory 비채택)

- MaxDeliver 초과 시 JetStream은 자동으로 DLQ로 옮기지 않음 — 재전달 중단 + advisory만.
- Aura 확정 경로: 마지막 delivery에서 payload를 `aura.dlq.>`로 복사한 뒤 `Term()`/`Ack`.
- WorkQueue에서는 MaxDeliver 이후 `stream get`이 실패할 수 있어 Advisory(②)만으로는 payload 유실 위험.
- Fission MQT wire-up은 후속(미들웨어); 계약 스모크는 `smoke-dlq-term.sh`.
- `errorTopic`(V0.3)과 역할 분리·병행.
