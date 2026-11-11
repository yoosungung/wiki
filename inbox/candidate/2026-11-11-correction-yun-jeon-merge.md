---
id: inbox-candidate-correction-yun-jeon-merge
agent: candidate
ticket_id: 91d3e50e-d890-4a24-ae97-dfe1e2827339
updated: 2026-11-11
status: inbox
sources:
  - ticket:91d3e50e-d890-4a24-ae97-dfe1e2827339
  - https://github.com/berryking404/candidate.win/issues/29
  - https://github.com/berryking404/candidate.win/pull/37
  - wiki/Engineering/AI-Native-Engineering/Candidate-Pages-Deploy-Not-Tenant-CD.md
  - wiki/Engineering/AI-Native-Engineering/Candidate-Sourceless-Stance-Takedown.md
---

# correction: yun-jeon → yun-seok-yeol

- GH #29 "윤전" stub은 윤석열(mangled "윤 전") — SSoT 삭제 후 canonical `yun-seok-yeol` aliases에 `윤전` 추가 + Hugo `aliases: [/people/yun-jeon/]` 리다이렉트.
- orphan people의 sourceless 미확인 stance는 canonical에 병합하지 않음; issue mirror 라인도 strip (Sourceless-Stance-Takedown).
- Done 게이트: Pages (`tenant_cd` N/A) — merge 후 live redirect + `test:`/`prod:`.
