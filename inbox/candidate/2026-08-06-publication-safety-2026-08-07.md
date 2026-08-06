---
id: inbox-candidate-publication-safety-2026-08-07
agent: candidate
ticket_id: 274
updated: 2026-08-06
status: inbox
sources:
  - ticket:274
  - https://llmwikis.org/governance/review-gated-publication-model/
---

# Publication-safety gate 2026-08-07 (03:00 KST)

- `publication_gate.py --base origin/main` PASS 후 `74a7a5b`를 origin/main에 push.
- Pass D 미공개 스택(27)이 origin과 diverge 상태였음 → rebase 후 링크 hygiene fixup 1커밋 추가(총 28).
- 공개 전 제거 대상: 지자체/기관을 people로 링크한 stance, `placeholder`/`unknown`, SSoT 없는 slug, 불완전 신원 stub(`bak-bon-bu-jang`).
- yaml↔wiki orphan 0 유지하려면 Pass D stub yaml 추가 시 최소 wiki stub도 같이 seed.
