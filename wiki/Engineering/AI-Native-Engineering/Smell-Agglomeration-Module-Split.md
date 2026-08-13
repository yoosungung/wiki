---
id: smell-agglomeration-module-split
title: "냄새 응집은 관심사 모듈로 쪼갠다"
status: canonical
owner: km
updated: "2026-08-13"
last_updated: "2026-08-13"
review_after: "2026-11-13"
sources:
  - ticket:684
tags: ["Engineering", "AI-Native", "Refactor", "Clean-Code"]
type: "wiki"
---

# 냄새 응집은 관심사 모듈로 쪼갠다

한 파일이 SSE stash + LLM 슬림 예산 + JSON sanitize처럼 **상호작용하는 관심사**를 키우면 변경 강도가 치솟는다. 고아 nit를 고치는 것보다 **경계 모듈**이 싸다.

## 패턴

```text
god.py  →  execute_sse_stash.py / llm_slim.py / json_sanitize.py
god.py  =  얇은 re-export (기존 import 경로 유지)
```

행위 변경 없이 쪼개고, 경계는 단위 테스트로 고정한다 (`from …god import …`가 깨지지 않게). clean-code CI 축과 맞춘다 — [[wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md]].

## 관련

- [[wiki/Engineering/AI-Native-Engineering/LLM-Tool-Payload-Context-Trim.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md]]
