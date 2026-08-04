---
id: inbox-pm-nl2sql-clean-code-gate
agent: pm
ticket_id: 113
updated: 2026-08-04
status: inbox
sources:
  - ticket:113
  - ticket:99
  - https://github.com/yoosungung/nl2sql
---

# nl2sql clean_code 주간 게이트 = CI backend 3단

- #99는 `clean_code`를 `ruff check`만 등록(AA 주간 discovery 최소).
- #113 intake 확정(Option A): `cd backend && uv sync --extra dev --locked && uv run ruff check . && uv run mypy src && uv run pytest` — `.github/workflows/ci.yml` backend job과 정합.
- 로컬 스모크(2026-08-04): ruff 0 · mypy 33 files 0 · pytest 169 passed ~2s.
- `ruff format --check`는 CI에 없고 다수 파일 drift → 주간 게이트에 넣지 말 것(후속).
- frontend lint / mcp cargo는 주간 AA 게이트에서 제외(CI job 분리·시간).
- tenant_cd / §2.8 feature Done 증거 루프: N/A (quality.yaml NF만).
