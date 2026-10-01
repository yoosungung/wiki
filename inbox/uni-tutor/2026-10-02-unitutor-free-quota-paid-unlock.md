---
id: inbox-uni-tutor-free-quota-paid-unlock
agent: uni-tutor
ticket_id: 1c2a889c-946d-4400-a376-d3d9584814d4
updated: 2026-10-02
status: inbox
sources:
  - ticket:1c2a889c-946d-4400-a376-d3d9584814d4
---

# UniTutor 무료 문답 일 5회 + 유료 스텁

- Product lock: 무료 TutorTurn **5**/일 (`<!-- free-tutor-turns:5 -->`).
- FE ledger `unitutor:tutor-quota` (UTC day·count·consumedTurnIds); 동일 `turn.id` 당일 재과금 없음.
- 유료 unlock은 `unitutor:entitlement` plan=paid 스텁 — 결제 벤더 없음. 광고/BYOK는 T3-04.
- Gate UI: `QuotaGate` CTA「유료로 문답 해제 (테스트)」.
