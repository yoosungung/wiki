---
id: inbox-nl2sql-clean-code-ci-align
agent: nl2sql
ticket_id: 113
updated: 2026-08-04
status: inbox
sources:
  - ticket:113
  - ticket:99
  - https://github.com/yoosungung/nl2sql/pull/25
---

# nl2sql clean_code = CI backend 3단

- `.factory/quality.yaml` `clean_code.command`은 ruff-only가 아니라 `uv sync --extra dev --locked && ruff check . && mypy src && pytest` (#113 Option A).
- `.factory/test_quality_yaml_nf.py`가 세 단계 존재를 assert한다.
- `ruff format --check`·frontend lint·mcp cargo는 주간 AA 게이트에서 제외(후속/CI job 분리).
