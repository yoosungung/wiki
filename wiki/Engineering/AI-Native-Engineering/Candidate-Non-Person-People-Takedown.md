---
id: candidate-non-person-people-takedown
title: "candidate.win: non-person /people stub takedown"
status: canonical
owner: km
updated: "2026-11-12"
last_updated: "2026-11-12"
review_after: "2027-02-12"
sources:
  - inbox/candidate/2026-11-11-takedown-jeong-bu-non-person.md
  - inbox/candidate/2026-11-11-takedown-bae-jae-go-non-person.md
  - inbox/pm/2026-11-11-takedown-jeong-bu-intent-closeout.md
  - inbox/pm/2026-11-11-takedown-bae-jae-go-intent-closeout.md
  - ticket:ee9febc4-a7f1-4ccc-ad34-ceb57e5736aa
  - ticket:d7107d79-c9be-4703-8228-5db789b00a1e
  - wiki/Engineering/AI-Native-Engineering/Candidate-Sourceless-Stance-Takedown.md
  - wiki/Engineering/AI-Native-Engineering/Candidate-Pages-Deploy-Not-Tenant-CD.md
tags: ["Engineering", "AI-Native", "candidate.win", "Moderation", "People"]
type: wiki
---

# candidate.win: non-person `/people` stub takedown

기관·학교 등 **인물이 아닌** slug가 `/people` stub으로 들어가면 SSoT yaml + wiki md를 **삭제**한다 (stance-only strip과 다름).

## 사례

| slug | 오분류 | 조치 |
| :--- | :--- | :--- |
| `jeong-bu` | name/role=`정부` | yaml+md 삭제 + 회귀 slug 리스트 |
| `bae-jae-go` | 배재고 · role=`고등학교 야구부` | 동일; 이슈 본문은 plain text 유지 |

회귀: `agent/tests/test_takedown_non_person_people_absent.py`에 slug 고정.

## Done 게이트

- merge → Pages Deploy success + **live** `/people/{slug}/` **404** = `prod:` (`tenant_cd` N/A).
- GH issue close는 live verify 후 수동.
- Own-authored PR은 `gh pr review --approve` 막힘 → Intent는 merge + ticket `intent: pass`.

## vs sourceless stance

[[wiki/Engineering/AI-Native-Engineering/Candidate-Sourceless-Stance-Takedown.md]]는 stub/page shell **유지** + stance strip. 본 페이지는 **페이지 제거**.

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Candidate-Pages-Deploy-Not-Tenant-CD.md]]
- [[wiki/Engineering/AI-Native-Engineering/Candidate-People-Slug-Alias-Redirect.md]]
