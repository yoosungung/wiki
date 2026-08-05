---
id: llm-tool-payload-context-trim
title: "LLM 도구 페이로드 컨텍스트 트림 (작은 context 모델)"
status: canonical
owner: km
updated: "2026-08-05"
last_updated: "2026-08-05"
review_after: "2026-11-05"
sources:
  - ticket:172
tags: ["Engineering", "AI-Native", "LLM", "Context", "Agents"]
type: "wiki"
---

# LLM 도구 페이로드 컨텍스트 트림 (작은 context 모델)

도구 결과는 정상인데 chat SSE가 `BadRequestError: input N > model context M`(예: 18k > 16k)로 끊기고 **`sql` 이벤트가 없다**. 원인 후보를 서빙 `--context-length` 올리기와 **도구 응답 슬림화**로 분리한다.

## 제품 쪽 트림 (우선)

| 대상 | 전형 조치 |
| :--- | :--- |
| describe/search 스키마 | relation `join`/`targetColumns` 등 LLM에 불필요한 그래프 fluff 제거 |
| valueDomain | members≤N, synonyms≤K 상한 |
| search `k` / preview rows | `k`≤3, preview≤8 등 하드캡 |
| 도구 호출 폭주 | FS/편집 도구 제외·recursion 상한 — [[wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md]] |

함수명은 제품별(`slim_describe_for_llm` 등)이나 요지는 **“도구 JSON을 모델 context 예산 안으로”**.

## 운영 쪽 대안

서빙 엔진(SGLang 등) `--context-length`를 여유(예: ≥~20k)로 올린다. 트림 후에도 부족할 때만. 클러스터 SGLang 메모는 [[wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md]].

## 진단 체크

1. MCP Host/인증이 200·401로 정상인가? (403 Host는 별축 — [[wiki/Engineering/Infrastructure-and-DevOps/MCP-Host-Allowlist-DNS-Rebinding.md]])
2. SSE에 tool 호출은 있으나 LLM BadRequest인가?
3. 트림 배포 후 동일 스모크에서 overflow가 사라졌는가? (그다음 hang/no-sql은 fail-fast 축)

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Agent-SSE-Failfast-and-Tool-Flood-Guard.md]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
- [[wiki/Engineering/Prompt-Engineering/Context-Engineering-Sessions-and-Memory.md]]
