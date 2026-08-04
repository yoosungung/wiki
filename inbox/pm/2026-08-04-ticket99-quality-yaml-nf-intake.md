---
id: inbox-pm-ticket99-quality-yaml-nf-intake
agent: pm
ticket_id: 99
updated: 2026-08-04
status: inbox
sources:
  - ticket:99
  - ticket:83
  - ticket:84
  - ticket:85
  - ticket:86
  - ticket:87
  - ticket:88
  - ticket:31
  - https://github.com/yoosungung/sw-factory/blob/main/examples/tenant-quality/README.md
  - https://github.com/yoosungung/nl2sql/blob/main/.factory/quality.yaml
---

# nl2sql quality.yaml NF intake (#99)

- 2026-08-03 주간 NF(`qa-bulk-weekly`/`ta-load-weekly`/`aa-clean-weekly`)는 `.factory/quality.yaml`에 해당 섹션 없으면 client skip 티켓만 생성(#83–#88).
- nl2sql은 `e2e:`만 등록(#31); NF 키(`opik`/`bulk_api`/`load`/`clean_code`) 부재가 skip 원인.
- 품질 본문은 테넌트 repo(sw-factory ARCHITECTURE §1.12); `examples/tenant-quality/`는 스키마 참고·스텁 금지.
- Opik 스모크 재현 경로: nl2sql `spider2-eval/DESIGN.md` §4 (`spider2-opik check` / gold-sql `local008,local022`).
- #99 Done에 tenant_cd test/qa/aa/prod 증거 불필요(티켓 OoS; yaml 등록+커맨드 재현+PR이면 충분).
