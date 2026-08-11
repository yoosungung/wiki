---
id: needs-only-aggregate-ci-gate
title: "needs-only 집계 CI 게이트 flake 가드"
status: canonical
owner: km
updated: "2026-08-11"
last_updated: "2026-08-11"
review_after: "2026-11-11"
sources:
  - ticket:391
tags: ["Engineering", "AI-Native", "CI", "GitHub-Actions"]
type: "wiki"
---

# needs-only 집계 CI 게이트 flake 가드

required job이 **제품 테스트 없이** `needs:`만 모아 echo/assert하는 집계 게이트면, runner 미배정·로그 blob timeout으로 **~수초 empty steps FAIL**이 날 수 있다. 하위 job(backend/lint/test)은 green인데 merge만 막힌다.

## 패턴

1. 집계 job에서 `needs.*.result`를 **명시 assert**(success/skipped 허용 집합).
2. empty steps / runner_id=0를 제품 회귀와 분리 — tip push로 재큐만 하거나, runner 복구는 **인간 Approval** 축.
3. Pod/`GH_TOKEN`에 `actions:write`가 없으면 `gh run rerun` 불가 → **빈 커밋/팁 push**로 재큐가 현실적 경로.

## 함정

- 집계 FAIL을 mypy/제품 실패로 오진하면 불필요한 코드 롤백이 난다.
- Actions runner 그룹 장애(`runner_id=0`)는 에이전트 kubectl/CD로 고치지 말고 Approval로 올린다.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/GHA-Workflow-PR-Only-Trigger.md]]
- [[wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md]]
