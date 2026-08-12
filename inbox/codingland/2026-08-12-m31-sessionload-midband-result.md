---
id: inbox-codingland-m31-sessionload-midband-result
agent: codingland
ticket_id: 544
updated: 2026-08-12
status: inbox
sources:
  - ticket:544
  - wiki/Engineering/AI-Native-Engineering/Epistemic-Debt-ChangeScore-Friction-Gate.md
---

# M3.1 sessionLoad mid-band 실험 결과 (#544)

- 조정: `SESSION_LOAD_PENALTY_MID` 0.10→0.15 (named constants). ROADMAP 미결정 유지.
- 검증: mean 0.72 @ sessionLoad 0.45 → full→light (0.10이면 0.62로 full 잔류). float로 mean≈0.70@0.45는 구 penalty에도 light였음.
- full-tier fixture는 mid-band 미만 sessionLoad로 회귀 고정 (gateSmoke/session).
