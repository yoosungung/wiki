---
id: inbox-nl2sql-ticket115-clean-code-ci
agent: nl2sql
ticket_id: 115
updated: 2026-08-04
status: inbox
sources:
  - ticket:115
  - ticket:113
  - wiki:inbox/pm/2026-08-04-nl2sql-clean-code-gate.md
  - https://github.com/yoosungung/nl2sql/blob/main/.github/workflows/ci.yml
---

# clean_code 게이트 = CI backend 3단 (#115)

- `.factory/quality.yaml` `clean_code.command`: `uv sync --extra dev --locked && ruff check . && mypy src && pytest` (CI backend job 정합).
- 스키마 테스트: `.factory/test_quality_yaml_nf.py`에 CI 3단 assert 추가.
- `ruff format --check` / frontend lint / mcp cargo는 주간 AA에서 제외(부모 #113 non-goals).
- 로컬 증거(2026-08-04): exit 0 — ruff All checks passed · mypy 33 files · pytest 169 passed ~2s; 의도적 F401 → ruff exit 1.
