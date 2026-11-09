---
id: inbox-pm-source-na-intent-drift
agent: pm
ticket_id: 38f15177-82cb-43c9-a7e0-549e9fda9a60
updated: 2026-11-09
status: inbox
sources:
  - ticket:38f15177-82cb-43c9-a7e0-549e9fda9a60
  - https://github.com/berryking404/candidate.win/pull/22
  - wiki/Engineering/AI-Native-Engineering/Hugo-External-Link-New-Tab.md
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
---

# candidate.win source N/A — Intent drift

- PR #22만으로는 Intent 부족: Hugo render 가드는 secondary; eric refine은 agent/SSoT에서 빈/`N/A` source 금지(유효 URL 필수 또는 stub 승격 fail).
- Publication-Gate 문서: 점수 게이트 ≠ 출처 게이트 — source-nonempty는 별도 필요.
- pm catch-up: `intent: drift`, merge 보류, assignee → candidate.
