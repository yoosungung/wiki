---
title: "Hierarchical-Memory-for-LLMs-계층적-메모리-구조"
related_raw: ["[[wiki/Agents/Memory-and-Cognition/Hierarchical-Memory-for-LLMs-계층적-메모리-구조.md]]"]
tags: ['wiki', 'knowledge_and_memory', 'advanced_rag_&_knowledge_graph', 'agent_memory_and_cognition']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Hierarchical Memory for LLMs: 계층적 메모리 구조

## 개요
LLM이 긴 문맥(Long Context)을 처리할 때 발생하는 비용과 성능 저하 문제를 해결하기 위해 컴퓨터 아키텍처의 캐시 계층과 유사한 '계층적 메모리' 시스템이 도입되었습니다. 이 시스템은 AI 에이전트가 방대한 데이터를 지능적으로 관리하고 필요한 때에 신속하게 불러올 수 있게 합니다.

## 메모리 계층 구조
*   **L1 (작업 메모리):** 현재 처리 중인 즉각적인 토큰과 활성화 상태를 유지하며 가장 빠른 응답 속도를 제공합니다.
*   **L2 (단기 에피소드 메모리):** 현재 대화 세션 내의 이전 맥락을 요약된 형태로 저장하여 컨텍스트 윈도우의 효율성을 극대화합니다.
*   **L3 (장기 지식 저장소):** 과거의 모든 상호작용과 외부 지식을 벡터화 및 지식 그래프화하여 저장합니다. Mem0, Cognee 등과 같은 도구가 이 계층의 지능형 검색(Retrieval)을 담당합니다.

## 핵심 특징 및 효과
*   **지능형 메모리 관리:** 모델이 무한에 가까운 컨텍스트를 가진 것처럼 작동하게 하여, 복잡한 프로젝트 관리나 연속적인 연구 작업에서 일관성을 유지할 수 있도록 돕습니다.
*   **비용 절감:** 불필요한 데이터를 컨텍스트 윈도우에 반복적으로 넣는 대신 필요한 정보만 인덱싱하여 불러오기 때문에 추론 비용을 획기적으로 낮출 수 있습니다.

## 원본 URL
- https://unite.ai/hierarchical-memory-for-llms

## 관련 링크
- [[wiki/Agents/Memory-and-Cognition/Mem0-vs-Cognee-vs-QMD-Comparison]]
- [[wiki/Agents/Memory-and-Cognition/Cognee - AI Memory System]]
- [[wiki/Agents/Memory-and-Cognition/Cognee 핵심 개념]]
- [[wiki/Agents/Memory-and-Cognition/LangMem]]
- [[wiki/Agents/Memory-and-Cognition/Memory]]
