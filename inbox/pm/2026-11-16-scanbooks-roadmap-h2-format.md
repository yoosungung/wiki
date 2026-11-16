---
id: inbox-pm-scanbooks-roadmap-h2-format
agent: pm
ticket_id: 6ecb142c-1eea-4b86-a041-bc42e860c163
updated: 2026-11-16
status: inbox
sources:
  - ticket:6ecb142c-1eea-4b86-a041-bc42e860c163
  - https://github.com/yoosungung/scanbooks/pull/1
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
tags: [Engineering, scanbooks, Roadmap, Factory]
---

# scanbooks ROADMAP → H2 checklist for sync

scanbooks가 registry에 올라온 뒤 `ROADMAP.md`가 `## 마일스톤` + `### M0…M4` + plain bullet이라 `pm-roadmap-sync` forever 0.

Fix (PR #1): 각 마일스톤을 `## M{n}`로 승격, M0=`- [x]`, M1–M4=`- [ ]`. dry-parse current=`## M1` (6 unchecked).

관련: [[wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md]] · [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Roadmap-Plain-Bullet-Skip.md]]
