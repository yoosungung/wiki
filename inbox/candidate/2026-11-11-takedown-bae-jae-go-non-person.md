---
id: inbox-candidate-takedown-bae-jae-go-non-person
agent: candidate
ticket_id: d7107d79-c9be-4703-8228-5db789b00a1e
updated: 2026-11-11
status: inbox
sources:
  - ticket:d7107d79-c9be-4703-8228-5db789b00a1e
  - https://github.com/berryking404/candidate.win/pull/34
  - https://github.com/berryking404/candidate.win/issues/28
  - wiki/Engineering/AI-Native-Engineering/Candidate-Pages-Deploy-Not-Tenant-CD.md
---

# takedown: bae-jae-go is a school, not a person

- `bae-jae-go` / 배재고 was a people stub with role `고등학교 야구부` — school org misfiled under `/people`.
- Fix: delete `data/people/bae-jae-go.yaml` + `wiki/content/people/bae-jae-go.md`; extend `test_takedown_non_person_people_absent` (with `jeong-bu`).
- Deploy path is GitHub Pages only (`tenant_cd` N/A). Done needs `test:` + live `prod:` 404 after merge.
- Issue pages already mention 배재고 as plain text (no `/people/bae-jae-go` links after prior hygiene).
