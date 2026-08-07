---
id: soft-ttd-in-process-replay-sandbox
title: "Soft TTD: in-process Replay 샌드박스 (call tape)"
status: canonical
owner: km
updated: "2026-08-07"
last_updated: "2026-08-07"
review_after: "2026-11-07"
sources:
  - https://tianpan.co/blog/2026-04-12-deterministic-replay-debugging-non-deterministic-ai-agents
tags: ["Engineering", "AI-Native", "TTD", "Replay", "Sandbox", "Living-Spec"]
type: "wiki"
---

# Soft TTD: in-process Replay 샌드박스 (call tape)

비결정적 에이전트/확장 런타임을 **VM 힙 롤백 없이** 재현할 때, 호출 테이프(record) → `replay`/`inject`/`hotReboot`을 **동일 프로세스**에서 돌리는 soft Time-Travel Debugging 패턴.

## 핵심 축

| 축 | 권장 | 비목표(후속) |
| :--- | :--- | :--- |
| Runner hosting | **in-process** IsolatedRunner | worker/VM heap rollback |
| Record | call tape + checkpoint cache | 전체 힙 스냅샷 |
| Controls | `replay(entry, break)` · `inject` · `hotReboot` → last checkpoint | cloud Mirror / ChangeScore |
| Sanitize | shallow: `maxDepth`≤3, namePatterns + AST-sensitive → `[REDACTED]`; deeper → `[MAX_DEPTH]`; leaf stringify | 깊은 그래프 완전 마스킹 |
| Living Spec | sidecar frontmatter `scenarioId` ↔ 테스트 1:1; unknown id **throw**(orphan 테스트 금지) | 외부 Graphify |

## Host 배선 (개념)

- Time Bar scrub → `timeline.onChangeEnd`
- Hot Reboot → `runner.hotReboot` + `timeline.cache` push

## 검증

```bash
# 패키지 로컬 (예: extension/)
npm test          # suites cover sanitize / replay / living-spec id
npm run compile   # host tsc clean
```

로컬 확장 패키지만이면 테넌트 `tenant_cd`/QA e2e/AA 게이트는 **N/A** — [[wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md]].

## 참고

- Soft TTD 배경: [Deterministic Replay Debugging for Non-Deterministic AI Agents](https://tianpan.co/blog/2026-04-12-deterministic-replay-debugging-non-deterministic-ai-agents)

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/In-Process-ASGI-Load-Harness-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
