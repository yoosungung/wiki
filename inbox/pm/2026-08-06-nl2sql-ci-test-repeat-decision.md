---
id: inbox-pm-nl2sql-ci-test-repeat
agent: pm
ticket_id: 263
updated: 2026-08-06
status: inbox
sources:
  - ticket:263
  - https://github.com/yoosungung/nl2sql/blob/main/.github/workflows/ci.yml
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
---

# nl2sql GHA CI: PR+push 이중 실행 vs 삭제

- nl2sql `ci.yml`은 `pull_request`와 `push`(main) 둘 다라 머지마다 backend+mcp-test가 반복된다(mcp-test ~9–10m이 wall 대부분).
- DuckDB PR job은 이미 제거됨; 전체 pytest/mcp-test 삭제는 PR 게이트·required checks와 충돌.
- 주간 `clean_code`(ruff+mypy+pytest)는 CI와 **정합** 목적의 Pod NF이며 GHA 중복 삭제로 다루면 안 됨.
- 비용 절감 1순위 후보: main `push` 트리거 축소(PR required checks 유지), 테스트 스위트 통삭제는 비권고.
