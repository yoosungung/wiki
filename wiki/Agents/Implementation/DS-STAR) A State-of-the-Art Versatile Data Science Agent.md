---
title: "DS-STAR) A State-of-the-Art Versatile Data Science Agent"
related_raw: ["[[wiki/Agents/Implementation/DS-STAR) A State-of-the-Art Versatile Data Science Agent.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'implementations', 'llm_agent_builders_research']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

DS-STAR는 Google Cloud의 윤진성(Jinsung Yoon)과 남재현(Jaehyun Nam)이 개발한 최첨단 다목적 데이터 과학 에이전트입니다. 통계 분석, 시각화, 데이터 랭글링 등 다양한 데이터 유형에 걸쳐 광범위한 데이터 과학 작업을 자동화하는 것을 목표로 합니다.

## DS-STAR의 주요 혁신

1.  **데이터 파일 분석 모듈:** 비정형을 포함한 다양한 데이터 형식에서 컨텍스트를 자동으로 추출합니다.
2.  **검증 단계:** LLM 기반 심사관이 각 단계에서 계획의 충분성을 평가합니다.
3.  **순차적 계획 프로세스:** 피드백을 기반으로 초기 계획을 반복적으로 구체화합니다.

## 작동 방식

DS-STAR는 두 가지 주요 단계로 작동합니다.

1.  디렉토리의 모든 파일을 자동으로 검사하고 구조와 내용에 대한 텍스트 요약을 만듭니다.
2.  계획, 구현 및 검증의 기본 루프에 참여합니다. Planner 에이전트는 상위 수준 계획을 만들고, Coder 에이전트는 이를 코드 스크립트로 변환하고, Verifier 에이전트(LLM 기반 심사관)는 코드의 효율성을 평가합니다. 불충분한 경우 Router 에이전트가 계획을 구체화하고 주기는 최대 10라운드까지 반복됩니다.

DS-STAR는 DABStep, KramaBench, DA-Code와 같은 벤치마크에서 최첨단 성능을 달성했으며, 특히 다양하고 이기종인 데이터 파일을 포함하는 작업에서 AutoGen 및 DA-Agent와 같은 기존 방법을 훨씬 능가합니다. 어블레이션 연구는 고성능 및 효과적인 계획 개선을 위한 데이터 파일 분석기 및 라우터 구성 요소의 중요성을 확인했습니다. 이 프레임워크는 또한 GPT-5와 같은 다양한 LLM에 대한 일반화 가능성을 보여줍니다.

## 원문 URL

*   https://research.google/blog/ds-star-a-state-of-the-art-versatile-data-science-agent/

## 링크

*   [[Archive/AI Agent 구성 (내부 교육용)]]
*   [[wiki/Agents/Multi-Agent-and-Orchestration/멀티-에이전트-패턴]]
*   [[wiki/Models/Reasoning-and-Cognition/Andrej_Karpathy_on_AGI]]
*   [[wiki/Models/RL/Parlant]]
*   [[wiki/Agents/Frameworks/Microsoft-Frameworks/Microsoft Agent Framework]]
*   [[wiki/Agents/Implementation/Agents 2.0 - From Shallow Loops to Deep Agents]]
*   [[wiki/Agents/Implementation/open-agent-builder]]
*   [[wiki/Agents/Memory-and-Cognition/OpenMemory]]
*   Resources/LLM-Concepts/LLM 학습 경로
*   Resources/LLM-Concepts/추출 Prompt 예시
*   [[wiki/Models/Reasoning-and-Cognition/Why LLM models are not good at RAG]]
*   [[wiki/Engineering/Prompt-Engineering/메타_프롬프트]]
*   [[wiki/Models/Reasoning-and-Cognition/LLM_Parallel_Thinking_Parallel-R1]]
*   [[wiki/Engineering/Prompt-Engineering/AI_질문법]]
*   [[wiki/Engineering/Prompt-Engineering/프롬프트_컨텍스트_엔지니어링]]
*   [[wiki/Engineering/Prompt-Engineering/LLM_Thinking_Time_Prompt_Engineering]]
*   Resources/Knowledge-Graph/상향식 지식 그래프 구축에서 온톨로지 정의
*   [[wiki/RAG/RAG-Anything - All-in-One RAG System]]
*   [[wiki/RAG/GraphRAG]]
*   Resources/Knowledge-Graph/LLM을 활용한 상향식 지식 그래프 구축
*   Resources/Knowledge-Graph/지식 그래프 기반 유사 법률 판례 검색 시스템
*   [[wiki/RAG/Knowledge Graph Extraction and Challenges]]
*   [[wiki/RAG/Apple_Embedding_Atlas_RAG_Optimization]]
*   Graphiti 1
*   [[wiki/RAG/GraphRAG - Part 2 - Implementation]]
*   [[wiki/RAG/GraphRAG - Part 4 - Microsoft Implementation]]
*   [[wiki/RAG/GraphReady]]
*   [[wiki/Agents/Frameworks/LangChain/custom_langchain_chat_model]]
*   [[Archive/law-agent/idea]]
*   [[Projects/LinkedIn/현대 AI 멀티에이전트 시스템의 구조와 동작]]
*   [[Projects/LinkedIn/Lake House ???]]
*   Projects/LinkedIn/농업 AI Agent 구성
*   Projects/LinkedIn/HyperCloveX로 ChatBot 만들기
*   Projects/LinkedIn/The Egg와 LLM 페르소나
*   [[wiki/Models/Multimodal-and-Vision/ByteDance Dolphin - Multimodal AI Model]]
*   [[wiki/Models/Optimization-and-Serving/oLLM_Lightweight_LLM_Inference_Library]]
*   [[wiki/Models/Reasoning-and-Cognition/KORMo-Team]]
*   [[wiki/Models/Multimodal-and-Vision/DeepSeek-OCR]]
*   [[wiki/Agents/Frameworks/Kotaemon]]
*   [[Archive/LGAI 교육]]
*   Areas/RAG기술현황(1)
*   Areas/RAG기술현황(2)
*   [[wiki/Agents/Frameworks/MCP/MCP]]
