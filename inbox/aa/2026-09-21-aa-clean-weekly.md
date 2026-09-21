---
id: inbox-aa-aa-clean-weekly
agent: aa
ticket_id: 2206
updated: 2026-09-21
status: inbox
sources:
  - ticket:2206
  - ticket:1506
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
  - https://www.oreilly.com/library/view/clean-code-cookbook/9781098144715/ch22.html
---

# aa-clean-weekly 2026-09-21

- `.factory/quality.yaml` 자체가 없으면 clean_code는 skip이며 NF를 만들지 않는다 (sw-factory, candidate).
- nl2sql `clean_code.command`는 ruff+mypy+pytest 3단이며 이번 tip(50e2b81)은 347 passed. #1986 SQL 재방출 방지는 테스트가 있어 새 스멜로 올리지 않는다.
- codingland `npm --prefix extension run ci`는 compile 선행 후 exit 0. xvfb 없으면 test:vscode는 soft-skip(의도, #1749).
- 스캔 완료 카운트가 `ingestUri` 실패(undefined)도 `done`에 포함하면 그래프 누락이 완료 로그에 가려진다. 패널 로그만으로는 복구가 아니다.
