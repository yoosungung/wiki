---
id: inbox-uni-tutor-ad-reward-turns
agent: uni-tutor
ticket_id: 8e3ba7e3-d77e-46b8-8359-72ef1b6f64d6
updated: 2026-10-02
status: inbox
sources:
  - ticket:8e3ba7e3-d77e-46b8-8359-72ef1b6f64d6
---

# UniTutor ad-reward tutor turns (+3 stub)

- Product lock: 광고 1회 → 문답 **3** (`<!-- ad-reward-tutor-turns:3 -->`). BYOK 노출은 후속.
- Ledger `unitutor:tutor-quota`에 `bonusTurns`; 유효 한도 = 5 + bonusTurns (UTC day 롤시 bonus 리셋).
- `grantAdReward` FE 스텁 — 광고 SDK/벤더 없음. QuotaGate CTA「광고 보고 3회 충전 (테스트)」.
