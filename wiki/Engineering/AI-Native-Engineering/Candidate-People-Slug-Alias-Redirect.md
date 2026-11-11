---
id: candidate-people-slug-alias-redirect
title: "candidate.win: mangled people slug → canonical alias"
status: canonical
owner: km
updated: "2026-11-12"
last_updated: "2026-11-12"
review_after: "2027-02-12"
sources:
  - inbox/candidate/2026-11-11-correction-yun-jeon-merge.md
  - ticket:91d3e50e-d890-4a24-ae97-dfe1e2827339
  - wiki/Engineering/AI-Native-Engineering/Candidate-Sourceless-Stance-Takedown.md
  - wiki/Engineering/AI-Native-Engineering/Candidate-Non-Person-People-Takedown.md
tags: ["Engineering", "AI-Native", "candidate.win", "People", "Alias"]
type: wiki
---

# candidate.win: mangled people slug → canonical alias

오타·잘린 표기 stub(예: GH #29「윤전」= 윤석열 mangled)은 삭제 후 **canonical** slug의 aliases에 표기를 넣고 Hugo `aliases:`로 리다이렉트한다.

## 계약

| 축 | 규칙 |
| :--- | :--- |
| SSoT | orphan stub yaml 삭제; canonical aliases에 mangled 표기 추가 |
| Hugo | `aliases: [/people/{mangled}/]` → canonical URL |
| Stance | orphan의 sourceless 미확인 stance는 canonical에 **병합 금지**; issue mirror strip ([[wiki/Engineering/AI-Native-Engineering/Candidate-Sourceless-Stance-Takedown.md]]) |
| Done | Pages live redirect + `test:`/`prod:` (`tenant_cd` N/A) |

예: `yun-jeon` → `yun-seok-yeol` + alias `윤전`.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Candidate-Non-Person-People-Takedown.md]]
- [[wiki/Engineering/AI-Native-Engineering/Candidate-Pages-Deploy-Not-Tenant-CD.md]]
