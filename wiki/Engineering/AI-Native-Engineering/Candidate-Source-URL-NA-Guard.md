---
id: candidate-source-url-na-guard
title: "candidate.win: source_url=N/A 가드 (Pass A + Hugo)"
status: canonical
owner: km
updated: "2026-11-10"
last_updated: "2026-11-10"
review_after: "2027-02-10"
sources:
  - inbox/candidate/2026-11-09-source-url-na-pass-a-guard.md
  - inbox/candidate/2026-11-09-source-href-na-render-guard.md
  - inbox/pm/2026-11-09-source-na-intent-drift.md
  - inbox/pm/2026-11-09-source-url-na-intent-pass-closeout.md
  - inbox/pm/2026-11-09-candidate-source-href-na.md
  - inbox/pm/2026-11-09-pm-checkpoint-source-na-ac-refine.md
  - inbox/pm/2026-11-09-pm-checkpoint-source-na-done.md
  - ticket:38f15177-82cb-43c9-a7e0-549e9fda9a60
  - https://github.com/berryking404/candidate.win/pull/22
  - https://wiki.candidate.win/people/i-si-ba/
tags: ["Engineering", "AI-Native", "candidate.win", "Pass-A", "Hugo"]
type: wiki
---

# candidate.win: source_url=N/A 가드 (Pass A + Hugo)

증상: Tier1 quote에 `source_url: "N/A"`가 truthy라 `_source_url_from_stance`가 크롤 fallback http(s)를 스킵하고 stance에 `[출처](N/A)`를 기록했다. Hugo는 이를 `<a href=N/A>`로 렌더해 상대경로로 잘못 이동했다. `quality_gate` Rule1이 empty URL만 강등하면 `N/A`는 Rule3 캐시미스로 통과한다.

## 정본 가드 (이중)

| 층 | 계약 |
| :--- | :--- |
| Pass A / quality_gate | `is_valid_source_url` = **http(s)만**. invalid quote skip → crawl fallback. 무효 URL은 강등. 유효 URL 없으면 stance 줄 생략. 기존 `[출처](N/A)`는 **미확인**으로 정리 |
| Hugo render | `wiki/layouts/_markup/render-link.html`: destination이 `http(s)://` 또는 `/`로 시작할 때만 `<a>`; 그 외는 `.Text`만. 동일 가드: `issues-single.html` source 표, `today/list.html` 대표 근거 |

## Intent 축

- PR #22 Hugo 가드만으로는 부족(secondary). eric refine: agent/SSoT에서 빈/`N/A` source 금지가 1차 — 유효 URL 필수 또는 stub 승격 fail.
- 점수 게이트 ≠ 출처 게이트 — [[wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md]].
- candidate.win Pages: tenant_cd N/A; Done 게이트 = `test:` + `prod:` (TA/QA/AA ladder 없음). merge `7920b23d` + Pages Deploy → prod `href=N/A`=0.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Hugo-External-Link-New-Tab.md]]
- [[wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md]]
