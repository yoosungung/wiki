---
id: quality-yaml-clean-code-ci-align
title: "quality.yaml clean_code = CI backend 3단 정합"
status: canonical
owner: km
updated: "2026-09-21"
last_updated: "2026-09-21"
review_after: "2026-12-20"
sources:
  - ticket:113
  - ticket:115
  - ticket:99
  - ticket:1751
  - ticket:1982
  - ticket:1983
  - ticket:2206
  - ticket:1749
  - https://github.com/npm/cli/issues/4139
  - https://github.com/kulshekhar/ts-jest/issues/3938
  - https://www.oreilly.com/library/view/clean-code-cookbook/9781098144715/ch22.html
  - inbox/codingland/2026-09-14-1982-ci-compile-before-host-test.md
  - inbox/aa/2026-09-14-clean-code-weekly.md
  - inbox/aa/2026-09-21-aa-clean-weekly.md
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

## 머지 충돌 시 `ci` 스크립트 보존 및 워크스페이스 컴파일 순서

충돌 해소로 `package.json`의 `"ci": "npm test && …"` 같은 **게이트 포인터**가 빠지면 clean_code/AA가 깨진다. 리팩터 PR을 합칠 때 기존 `ci`/`test:vscode` 키를 한쪽 브랜치에서만 갖고 있으면 **양쪽을 유지**한 뒤 CI를 다시 돌린다.

- **npm workspaces topo-sort 부재**: npm workspaces는 패키지 간 의존 관계에 따라 스크립트를 위상 정렬(topo-sort)하여 실행하지 않는다. 또한 `ts-jest`는 프로젝트 레퍼런스를 자동으로 빌드하지 않는다.
- **컴파일 선행 필수**: 호스트 단위 테스트(Jest)가 내부 패키지의 빌드 산출물(`dist/`의 `main` 및 `types`)을 참조하는 구조라면, `ci` 스크립트는 반드시 컴파일이 테스트보다 앞서야 한다:
  ```json
  "ci": "npm run compile && npm test && npm run test:vscode"
  ```
- **순서 가드**: `scripts/packageScripts.test.cjs` 등 정적 스크립트 테스트에서 `ci` 정의 문자열 내 `npm run compile`이 `npm test`보다 먼저 등장하는지 assert하여 스크립트 드리프트를 방지한다.
- **헤드리스 soft-skip**: `npm --prefix extension run ci`는 compile 선행 후 exit 0이 정본. `xvfb`가 없으면 `test:vscode`는 **의도적 soft-skip**(실패 아님). 주간 AA는 soft-skip을 NF로 올리지 않는다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Workspace-Ingest-Done-Vs-Skipped-Counter.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
