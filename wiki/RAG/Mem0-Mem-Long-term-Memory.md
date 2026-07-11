---
title: Mem0-Mem-Long-term-Memory
related_raw:
  - "[[wiki/RAG/Mem0-Mem-Long-term-Memory]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - mem0_cognee_claude-mem_long-term_memory
type: wiki
status: draft
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# Mem0: AI 에이전트를 위한 지능형 장기 기억 계층 (2026-04-11)

## 요약
Mem0는 LLM 애플리케이션을 위한 **지능형 자가 개선 메모리 계층**입니다. 단순한 대화 기록 저장을 넘어, 대화 내용을 고도로 최적화된 메모리 표현으로 압축하여 저장합니다. 프롬프트 토큰 사용량을 최대 80%~90%까지 절감하면서도 문맥의 충실도를 유지하는 '메모리 압축 엔진'과 하이브리드(Vector + Graph + KV) 아키텍처가 핵심입니다.

## 주요 특징
- **하이브리드 아키텍처:** 벡터 검색(유사성), 지식 그래프(관계성), Key-Value 스토어를 결합하여 정확도와 추론 능력을 동시에 확보.
- **토큰 효율성:** 전체 컨텍스트를 프롬프트에 넣는 방식 대비 토큰 사용량 90% 절감, 지연 시간(Latency) 91% 감소 달성.
- **사용자 개인화:** 사용자의 과거 선호도, 습관, 특정 정보를 장기적으로 기억하여 초개인화된 경험 제공.

## 기술적 시사점
에이전트가 과거의 실패와 피드백을 통해 스스로 성능을 개선하는 '자기 개선 루프'의 핵심 요소로 메모리가 자리 잡고 있습니다. 컨텍스트 윈도우의 물리적 한계를 효율적으로 극복할 수 있는 실질적인 대안입니다.

## 원본 링크
- [Mem0 Official Site](https://mem0.ai)

## 관련 노트
- [[wiki/Agents/Memory-and-Cognition/Cognee.md|Cognee: 지식 그래프 기반 메모리]]
- [[wiki/Engineering/Infrastructure-and-DevOps/AOI-Autonomous-RCA-2026.md|AOI: 자율 RCA와 지식 그래프 연동]]
- [[2026-04-11.md|2026-04-11 데일리 노트]]
