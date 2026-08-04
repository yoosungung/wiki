---
id: quality-yaml-clean-code-ci-align
title: "quality.yaml clean_code = CI backend 3단 정합"
status: canonical
owner: km
updated: "2026-08-04"
last_updated: "2026-08-04"
review_after: "2026-11-04"
sources:
  - ticket:113
  - ticket:115
  - ticket:99
tags: ["Engineering", "AI-Native", "Quality", "CI", "Ruff", "Mypy"]
type: "wiki"
---

# quality.yaml clean_code = CI backend 3단 정합

주간 AA `clean_code`가 **ruff-only**면 CI backend job과 어긋나 주간에만 통과하는 드리프트가 난다. 게이트 커맨드를 CI와 **동일 3단**으로 맞춘다.

## 패턴

```yaml
# .factory/quality.yaml (개념)
clean_code:
  command: >-
    cd backend && uv sync --extra dev --locked
    && uv run ruff check .
    && uv run mypy src
    && uv run pytest
```

스키마 테스트로 “세 단계 존재”를 assert한다 (예: `test_quality_yaml_*.py`).

## 주간에서 빼는 것

| 항목 | 이유 |
| :--- | :--- |
| `ruff format --check` | CI에 없고 drift 많으면 상시 red |
| frontend lint | 별도 CI job·시간 |
| 언어별 sidecar (예: mcp cargo) | 주간 AA 스코프 밖 |

키 자체가 없으면 skip — [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]. stub `echo`를 examples에서 복사하지 않는다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
