---
id: inbox-candidate-people-ssot-curation-2026-09-03
agent: candidate
ticket_id: null
updated: 2026-09-03
status: inbox
sources:
  - ticket:candidate.win-people-curation-2026-09-03
  - https://www.yna.co.kr/view/AKR20260829044100001
  - https://www.newsis.com/view/NISX20250813_0003289476
---

# People SSoT curation 18:00 KST (2026-09-03)

- Prefer promote only with ≥1 safe-host `official_urls`/`profile_urls` (assembly/go.kr/yna/newsis/…).
- Pass-stack ahead commits may land with yaml-only people stubs; curation must add wiki shells before SSoT alignment tests pass.
- Local hook may divert unpushed pass-stack + shells onto `agent/pass-stack-preserve-*`; cherry-pick curation commits back onto `main` before push.
- publication_gate exit 0 is the validation gate for main push when Pass D commits are also ahead.
