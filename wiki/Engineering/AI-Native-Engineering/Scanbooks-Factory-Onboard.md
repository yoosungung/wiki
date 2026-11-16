---
id: scanbooks-factory-onboard
title: "scanbooks factory onboard + ROADMAP H2"
status: canonical
owner: km
updated: "2026-11-17"
last_updated: "2026-11-17"
review_after: "2027-02-17"
sources:
  - inbox/pm/2026-11-16-scanbooks-factory-onboard-complete.md
  - inbox/pm/2026-11-16-scanbooks-roadmap-h2-format.md
  - ticket:b0724db0-5ab9-4f50-8601-955482601a3f
  - https://github.com/yoosungung/scanbooks/pull/1
  - wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Factory-Onboard.md
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
tags: ["Engineering", "scanbooks", "Factory", "Onboard", "Roadmap"]
type: wiki
---

# scanbooks factory onboard + ROADMAP H2

| 축 | 값 |
| :--- | :--- |
| project_id | `4ad723c6-7d6d-4a98-81df-3ad3334a3188` |
| sessions user | `scanbooks@example.com` |
| repo | `yoosungung/scanbooks` |

## Onboard

- Client membership + staff lanes (ta/qa/aa/km) + `agents.yaml` sessions + workspace seed (uni-semantic pattern).
- Host: seed-personas + LaunchAgent restart after `agents.yaml` change.

## ROADMAP H2 for sync

- Before: `## 마일스톤` + `### M0…M4` + plain bullet → `pm-roadmap-sync` forever 0.
- Fix (PR #1): each milestone → `## M{n}`; M0=`- [x]`, M1–M4=`- [ ]`. dry-parse current=`## M1` then later `## M2`.
- Pattern: [[wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md]] · [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Roadmap-Plain-Bullet-Skip.md]].

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Factory-Onboard.md]]
- [[wiki/Engineering/AI-Native-Engineering/Scanbooks-M1-DocTr-Onnx-Latency.md]]
- [[wiki/Engineering/AI-Native-Engineering/Scanbooks-M2-App-Skeleton.md]]
