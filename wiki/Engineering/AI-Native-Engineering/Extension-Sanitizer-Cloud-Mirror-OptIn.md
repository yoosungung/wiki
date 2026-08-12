---
id: extension-sanitizer-cloud-mirror-optin
title: "확장 Sanitizer + Cloud Mirror 옵트인"
status: canonical
owner: km
updated: "2026-08-12"
last_updated: "2026-08-12"
review_after: "2026-11-12"
sources:
  - ticket:541
  - ticket:542
  - ticket:543
  - https://code.visualstudio.com/api/references/contribution-points
  - https://github.com/veryfront/veryfront-code/blob/main/src/utils/logger/redact.test.ts
tags: ["Engineering", "AI-Native", "VSCode", "Sanitizer", "Mirror", "Privacy"]
type: "wiki"
---

# 확장 Sanitizer + Cloud Mirror 옵트인

IDE 확장이 로컬 Mirror를 기본으로 두고 클라우드 경로를 **옵트인**할 때, 클라우드로 나가기 전 입력을 Sanitizer로 고정한다.

## Sanitizer 규칙 (개념)

| 규칙 | 요지 |
| :--- | :--- |
| `namePatterns` | substring + 대소문자 무시 |
| `astSensitiveParams` | **exact key**만 |
| depth 예산 | 배열 스텝도 카운트; `depth >= maxDepth` → `[MAX_DEPTH]` 후 leaf stringify 중단 |
| redact | 하위 미탐색 |
| 회귀 축 | 입력 비변이, root array, Runner·Mirror 공용 `DEFAULT_SANITIZE_OPTIONS` |

로컬 Jest만이면 tenant_cd/QA/AA prod 게이트는 Soft-TTD 기준 N/A — [[wiki/Engineering/AI-Native-Engineering/Soft-TTD-In-Process-Replay-Sandbox.md]].

## Cloud Mirror 옵트인

```text
contributes.configuration boolean  default: false
resolveMirrorAdapter → local Heuristic | CloudMirrorAdapter
livingSpecSeed JSON → sanitize → draft  (실 HTTP/키는 후순위)
```

실 Ollama vs node-llama 고착 전에 **stub만으로 경계**를 고정한다. core는 vscode-free — [[wiki/Agents/Coding-and-Engineering/VSCode-Extension-Pure-Core-Host-Split.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Epistemic-Debt-ChangeScore-Friction-Gate.md]]
- [[wiki/Agents/Coding-and-Engineering/VSCode-Extension-Pure-Core-Host-Split.md]]
- [[wiki/Engineering/AI-Native-Engineering/Soft-TTD-In-Process-Replay-Sandbox.md]]
