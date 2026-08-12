---
id: inbox-codingland-m31-sessionload-weight-tuning
agent: codingland
ticket_id: 544
updated: 2026-08-12
status: inbox
sources:
  - ticket:544
  - wiki/Engineering/AI-Native-Engineering/Epistemic-Debt-ChangeScore-Friction-Gate.md
  - https://doi.org/10.48550/arxiv.2602.20206
---

# M3.1 sessionLoad 가중치 튜닝 intake (#544)

- L0 실험 기본값: mean severity − step penalty(≥0.7→0.25, ≥0.4→0.10); tier 0.3/0.6; bypass=criticality<0.7 or sessionLoad≥0.5. 공식 고정은 ROADMAP 미결정.
- 테스트 갭: mid-band(−0.10)와 light→none 하향 경계가 Jest에 거의 없음 — 튜닝 전후 매트릭스가 AC 증거.
- wiki `Epistemic-Debt-ChangeScore-Friction-Gate`의 attempt===3 Bypass 금지는 ARCHITECTURE §1.9(attempt 비사용)와 충돌 — km 정리 후보; IC는 L0 따름.
