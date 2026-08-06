---
id: gha-workflow-pr-only-trigger
title: "GHA CI: PR-only 트리거 (main push 재실행 제거)"
status: canonical
owner: km
updated: "2026-08-06"
last_updated: "2026-08-06"
review_after: "2026-11-06"
sources:
  - ticket:263
  - https://adamj.eu/tech/2025/05/14/github-actions-avoid-simple-on/
tags: ["Engineering", "AI-Native", "CI", "GitHub-Actions", "Cost"]
type: "wiki"
---

# GHA CI: PR-only 트리거 (main push 재실행 제거)

`pull_request`와 `push`(main)를 동시에 켜면 **머지마다 동일 게이트가 두 번** 돈다(특히 장시간 job). 비용·큐 절감 1순위는 **main `push` 트리거 제거**, PR required checks는 유지.

## 패턴

```yaml
# .github/workflows/ci.yml (개념)
on:
  pull_request:
  # push:  # main/master — 제거(Option B)
```

- 릴리스 미러·패키지 publish 워크플로(`publish-releases.yml` 등)의 `push`는 **별축** — ci.yml과 혼동하지 않는다.
- 주간 Pod NF(`clean_code` 등)는 CI 정합용이며 GHA 중복 삭제로 다루지 않는다 — [[wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md]].

## PyYAML `on` 함정

PyYAML 1.1은 키 `on`을 bool `True`로 파싱한다. 워크플로 트리거 단언 시:

```python
data.get("on", data.get(True))
```

참고: [Avoid the simple name `on`](https://adamj.eu/tech/2025/05/14/github-actions-avoid-simple-on/).

## 결정 가이드

| 후보 | 권고 |
| :--- | :--- |
| main push CI 제거 | 1순위 (PR gates 유지) |
| 전체 pytest/mcp-test 삭제 | 비권고 — required checks·PR 게이트와 충돌 |
| DuckDB 등 부가 PR job만 제거 | 이미 제거된 경우 재도입 금지 |

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
