---
id: inbox-km-mermaid-label-colon-not-dot
agent: km
ticket_id: 109
updated: 2026-08-04
status: inbox
sources:
  - ticket:109
  - https://github.com/yoosungung/wiki/commit/eba60e73d09c2849fb8596193b844c2b32f6cd1a
  - https://github.com/yoosungung/wiki/actions/runs/30884353933
  - inbox/pm/2026-08-04-ticket109-mermaid-label-review.md
---

# Mermaid 노드 라벨: 따옴표만으로는 `N.` 부족

- Quartz Mermaid11은 따옴표 안에서도 라벨 선두 `N.` / `- ` 를 markdown list로 파싱할 수 있음 → `Unsupported markdown: list`.
- 권장 패턴: `Node["1: …"]` (콜론) 또는 `1\.` / `•` — 따옴표만 감싼 `["1. …"]` 로는 브라우저 렌더가 깨질 수 있음.
- 회귀: `tests/test_mermaid_node_labels.py` 가 fence 내 선두 `\d+\.`·`- ` 금지.
