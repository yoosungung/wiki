---
id: inbox-pm-m31-sessionload-midband-decision
agent: pm
ticket_id: 544
updated: 2026-08-12
status: inbox
sources:
  - ticket:544
  - ticket:541
  - wiki/Engineering/AI-Native-Engineering/Epistemic-Debt-ChangeScore-Friction-Gate.md
  - https://dev.to/ktamarapalli/risk-adaptive-friction-designing-human-aware-security-controls-in-cicd-2m19
---

# M3.1 sessionLoad mid-band penalty — PM 결정 (#544)

- 제안 A 승인: mid-band (`sessionLoad≥0.4`) penalty `0.10→0.15` (실험값; 공식 고정 아님).
- 문서 범위: named constants + DESIGN 실험표 동기화만. ROADMAP 「미결정」 유지.
- Non-goals 유지: equal-mean 교체, bypass attempt 카운트, sessionLoad 텔레메트리 소스 신규, #542/#543 범위.
- 근거: mid-load에서 full→light 하향을 더 자주 유도; wiki 실험 기본값·adaptive friction(부하에 비례한 개입) 축과 정합.
- Done 기준: core Jest + gateSmoke; tenant_cd N/A (로컬 확장) → Review=git-ship+PR, Done=PR+tests closeout.
