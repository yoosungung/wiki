---
id: inbox-nl2sql-ci-pr-only-trigger
agent: nl2sql
ticket_id: 263
updated: 2026-08-06
status: inbox
sources:
  - ticket:263
  - https://github.com/yoosungung/nl2sql/blob/main/.github/workflows/ci.yml
  - https://adamj.eu/tech/2025/05/14/github-actions-avoid-simple-on/
  - inbox/pm/2026-08-06-nl2sql-ci-test-repeat-decision.md
---

# nl2sql CI: PR-only trigger (Option B)

- Eric 확정 B: `.github/workflows/ci.yml`에서 `on.push`(main/master) 제거, `pull_request`만 유지.
- 머지 후 main push 재실행(~mcp-test 9–10m)만 끊고 PR 게이트(backend/mcp-clippy/mcp-test/mcp)는 유지.
- PyYAML 1.1은 키 `on`을 bool `True`로 파싱하므로 워크플로 트리거 단언 시 `data.get("on", data.get(True))` 필요.
- publish-releases.yml의 push 트리거는 별개(릴리스 미러) — ci.yml과 혼동 금지.
