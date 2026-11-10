---
id: candidate-sourceless-stance-takedown
title: "candidate.win: sourceless 미확인 stance takedown"
status: canonical
owner: km
updated: "2026-11-11"
last_updated: "2026-11-11"
review_after: "2027-02-11"
sources:
  - inbox/candidate/2026-11-11-takedown-i-si-ba-sourceless.md
  - inbox/pm/2026-11-11-pm-checkpoint-takedown-i-si-ba-intent.md
  - inbox/pm/2026-11-11-takedown-i-si-ba-intent-closeout.md
  - ticket:d9210245-6a31-4384-b6f7-dc986c0c8616
  - https://github.com/berryking404/candidate.win/issues/23
  - https://github.com/berryking404/candidate.win/pull/32
  - wiki/Engineering/AI-Native-Engineering/Candidate-Source-URL-NA-Guard.md
tags: ["Engineering", "AI-Native", "candidate.win", "Moderation", "Stance"]
type: wiki
---

# candidate.win: sourceless 미확인 stance takedown

`quality_gate` Rule1이 원문 `미확인`을 스킵하면, `[출처](http(s):…)` 없는 **미확인** stance가 라이브 people 페이지에 남을 수 있다(Hugo가 미확인을 숨긴다는 DESIGN 노트와 불일치).

## 범위

| 축 | 계약 |
| :--- | :--- |
| Strip | people page의 sourceless stance만 (`agent:stances` empty). stub yaml + page shell **유지** |
| Mirror | 이슈 페이지 people 링크도 제거 — 안 하면 claim이 issue에 잔존 |
| Non-goal | 페이지 전체 wipe · auto-close GH issue · auto invent 새 stance |

## Done 게이트

- Intent: content-only strip (예: PR #32).
- `tenant_cd` N/A — GH Pages. merge → Pages Deploy success + **live** people empty stances = `prod:`.
- GH issue close는 사람이 live verify 후 수동(예: #23). 패턴: takedown AC에 `prod:` live check 필수.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Candidate-Source-URL-NA-Guard.md]]
- [[wiki/Engineering/AI-Native-Engineering/Candidate-Pages-Deploy-Not-Tenant-CD.md]]
- [[wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md]]
