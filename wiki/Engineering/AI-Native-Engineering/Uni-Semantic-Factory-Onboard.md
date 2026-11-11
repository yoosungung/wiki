---
id: uni-semantic-factory-onboard
title: "uni-semantic factory onboarding"
status: canonical
owner: km
updated: "2026-11-12"
last_updated: "2026-11-12"
review_after: "2027-02-12"
sources:
  - inbox/pm/2026-11-11-uni-semantic-factory-onboard.md
  - ticket:4ae933b7-93a5-40d3-8564-9a33dcf31dab
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
tags: ["Engineering", "uni-semantic", "Factory", "Onboard"]
type: wiki
---

# uni-semantic factory onboarding

| 축 | 값 |
| :--- | :--- |
| project_id | `120b0eb1-39cd-40cb-a70c-5a16aecbb61a` |
| sessions user | `uni-semantic@example.com` |
| repo | `yoosungung/uni-semantic` |

## 함정

- Client membership은 **owner-only** — 없으면 project member add → `not_client_member`.
- Persona overlay 없으면 `deploy/personas/_default`만 (aura/crewrp와 동일).
- Ops host: gateway+cursor LaunchAgents는 **macmini-server**; agents.yaml refresh/restart는 그 호스트에서.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Uni-Semantic-Roadmap-Plain-Bullet-Skip.md]]
- [[wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md]]
