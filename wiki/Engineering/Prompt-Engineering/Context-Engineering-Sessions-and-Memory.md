---
title: "Context-Engineering-Sessions-and-Memory"
related_raw: ["[[wiki/Engineering/Prompt-Engineering/Context-Engineering-Sessions-and-Memory.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'basetech', 'llm_agent_theory_and_patterns']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

Ivan Nardini가 발표한 AI 에이전트 구축을 위한 개발자 가이드 "Context Engineering: Sessions and Memory" 백서에 대한 요약입니다.

## 기술적 요약

이 백서는 에이전트 내 메모리의 전체 수명 주기를 다루며, 주요 내용은 다음과 같습니다:

*   **생성(Generation):** 노이즈가 많은 데이터 소스에서 통찰력을 추출합니다.
*   **통합(Consolidation):** LLM이 메모리를 병합, 업데이트, 정리하여 일관된 지식 기반을 유지합니다.
*   **검색(Retrieval):** 관련성, 최신성, 중요성을 고려하여 적절한 메모리를 찾습니다.
*   **추론(Inference):** 검색된 메모리를 컨텍스트 창에 배치하여 LLM의 추론에 영향을 미칩니다.

## 관련 논의

*   **외부 데이터베이스 사용:** Firebase, MongoDB, Redis와 같은 외부 데이터베이스를 메모리 저장소로 사용하는 것에 대한 논의가 있었습니다.
*   **메모리 관리자 계층:** 압축 유형, 이벤트/컨텍스트/스케줄 기반 트리거, 장기/단기/에피소드 기억 경로 등에 대한 심층적인 논의가 있었습니다.
*   **컨텍스트 엔지니어링:** 프로덕션 시스템에서는 프롬프트 엔지니어링보다 컨텍스트 엔지니어링이 더 적합하다는 의견이 제시되었습니다.

## 관련 링크

*   **백서 링크:** [https://lnkd.in/euud4BUB](https://lnkd.in/euud4BUB)
*   **Introduction to Agents 백서:** [https://lnkd.in/ekKF9Rz9](https://lnkd.in/ekKF9Rz9)
*   **계층적 메모리(H-MEM) 논문:** [https://lnkd.in/eTFeidvj](https://lnkd.in/eTFeidvj)
*   **Tiny Recursive Model(TRM) 논문:** [https://lnkd.in/dEJGF39K](https://lnkd.in/dEJGF39K)

## 관련 노트

*   [[wiki/Agents/Memory-and-Cognition/OpenMemory]]
*   [[Areas/RAG기술현황(1)]]
*   [[Areas/RAG기술현황(2)]]
*   [[Projects/LinkedIn/현대 AI 멀티에이전트 시스템의 구조와 동작]]

