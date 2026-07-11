---
title: "LangMem"
related_raw: ["[[wiki/Agents/Memory-and-Cognition/LangMem.md]]"]
tags: ['wiki', 'knowledge_and_memory', 'advanced_rag_&_knowledge_graph', 'agent_memory_and_cognition']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

### 2.3. LangMem: 절차적 기억과 자기 진화형 에이전트

**2.3.1. 아키텍처: 기억의 3원칙 (Semantic, Episodic, Procedural)** LangChain 팀이 개발한 LangMem은 인지 과학의 기억 분류 체계를 AI 에이전트에 도입했습니다. 특히 **절차적 기억(Procedural Memory)**의 구현은 다른 패키지들과 차별화되는 가장 큰 특징입니다. 절차적 기억이란 "자전거 타는 법"처럼 작업을 수행하는 방법에 대한 지식입니다. LangMem에서 이는 에이전트가 과거의 성공과 실패 경험을 분석하여 자신의 **시스템 프롬프트(System Prompt)를 스스로 수정(Update)**하거나, 도구 사용 전략을 최적화하는 형태로 구현됩니다.   

**2.3.2. LangGraph 통합 및 백그라운드 관리** LangMem은 독립적인 서비스라기보다 LangChain 생태계, 특히 **LangGraph**의 확장 모듈에 가깝습니다. LangGraph의 영구 저장소 계층(Long-term Memory Store)과 네이티브하게 통합되며, Pydantic 스키마를 통해 저장할 데이터의 타입을 엄격하게 정의할 수 있습니다. 또한, 대화의 흐름을 방해하지 않는 **백그라운드 메모리 관리자(Background Memory Manager)**를 제공합니다. 에이전트가 사용자와 대화하는 'Hot-path'와 별도로, 백그라운드 워커가 대화 로그를 분석하여 중요한 정보를 추출하고, 중복을 제거하며, 기억을 압축(Consolidation)합니다.   

**2.3.3. 성능 특성 및 적합성** LangMem은 실시간 응답 속도보다는 **기억의 품질과 에이전트의 성장**에 초점을 맞춥니다.

- **높은 지연 시간:** 일부 벤치마크에서 LangMem은 검색 및 처리 과정에서 60초 이상의 매우 높은 지연 시간을 보였습니다. 이는 LangMem이 기억을 인출할 때마다 복잡한 추론 과정을 거치거나, 다수의 LLM 호출을 수행하여 최적의 기억을 재구성하기 때문입니다.   
    
- **적합한 사용 사례:** 실시간 챗봇보다는 긴 호흡으로 연구를 수행하는 'Research Agent'나, 수일에서 수주에 걸쳐 코드를 작성하는 'Coding Agent' 등 스스로 학습하고 전략을 수정해야 하는 고도화된 에이전트에 적합합니다.