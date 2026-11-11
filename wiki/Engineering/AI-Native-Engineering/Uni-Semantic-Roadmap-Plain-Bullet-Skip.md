---
id: uni-semantic-roadmap-plain-bullet-skip
title: "uni-semantic ROADMAP plain-bullet → sync skip"
status: canonical
owner: km
updated: "2026-11-12"
last_updated: "2026-11-12"
review_after: "2027-02-12"
sources:
  - inbox/pm/2026-11-11-uni-semantic-roadmap-sync-plain-bullets.md
  - inbox/pm/2026-11-12-roadmap-sync.md
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
tags: ["Engineering", "uni-semantic", "Roadmap", "Factory"]
type: wiki
---

# uni-semantic ROADMAP plain-bullet → sync skip

`pm.roadmaps` / `roadmap-registry.json`에 `uni-semantic`이 있어도, `ROADMAP.md` Phase가 plain `-` bullet만 쓰면 everyday sync **current=없음**, pass-gate도 `skip: no passed section`.

Sync는 tenant ROADMAP을 rewrite하지 않음. Fix: Phase를 `- [ ]`/`- [x]`로 바꾸거나 narrative 유지+수동 티켓.

## 2026-11-12 관측

- crewrp: prior mile/child 404(project wipe) → recreate milestone + child.
- aura: incomplete 0 + no passed → skip; tickets=0.
- uni-semantic: Phase 2 checkbox 등장 후 milestone+children enqueue 가능 (plain→checkbox 전환 시점부터).

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md]]
- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Factory-Onboard.md]]
