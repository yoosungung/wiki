---
id: inbox-candidate-takedown-jeong-bu-non-person
agent: candidate
ticket_id: ee9febc4-a7f1-4ccc-ad34-ceb57e5736aa
updated: 2026-11-11
status: inbox
sources:
  - ticket:ee9febc4-a7f1-4ccc-ad34-ceb57e5736aa
  - https://github.com/berryking404/candidate.win/issues/27
  - https://github.com/berryking404/candidate.win/pull/33
  - wiki/Engineering/AI-Native-Engineering/Candidate-Pages-Deploy-Not-Tenant-CD.md
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
---

# candidate.win non-person /people takedown (jeong-bu)

- `people/jeong-bu` SSoT·wiki는 name_ko=`정부`, role=`정부` stub — 인물 아님 → 삭제(유지 사유 없음).
- 이슈 stance에 `/people/jeong-bu` 링크는 이미 없음(이전 hygiene delink). 삭제 대상은 yaml+md만.
- 회귀: `agent/tests/test_takedown_non_person_people_absent.py` 에 slug 고정.
- CD: Pages (`tenant_cd` N/A). Done=`test:`+`prod:` live 404. GH issue close는 live verify 후 수동.
