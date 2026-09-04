---
title: "PageIndex: 벡터 검색 없는 추론 기반 오픈소스 RAG 프레임워크"
last_updated: "2026-09-04"
updated: "2026-09-04"
related_raw: ["[[PageIndex Open-Source RAG Framework for Document Retrieval | Sumanth P님이 토픽에 대해 올림 | LinkedIn.md]]", "[[2026-09-04-openkb-persistent-wiki-compiler-pageindex.md]]"]
tags: ["RAG", "Vectorless", "Reasoning-based", "Search", "Open_Source", "PageIndex", "OpenKB"]
type: "wiki"
status: "published"
---

# PageIndex: 벡터리스 추론 기반 RAG의 새로운 지평

## 1. 개요
PageIndex는 전통적인 벡터 임베딩(Vector Search)에 의존하지 않고, LLM의 **추론 능력(Reasoning)**을 활용하여 문서를 검색하고 답변을 생성하는 차세대 오픈소스 RAG 프레임워크입니다. 벡터 데이터베이스의 인덱싱 오버헤드와 시맨틱 유사도의 한계를 극복하기 위해 설계되었습니다.

## 2. 핵심 메커니즘: 벡터리스 추론 (Vectorless Reasoning)
기존 RAG가 "유사한 텍스트 덩어리"를 찾는 데 집중했다면, PageIndex는 "질문에 답변하기 위해 필요한 정보가 어디에 있는가"를 추론합니다.
- **문서 구조 파악**: 문서의 레이아웃, 목차, 시각적 계층 구조를 보존하며 인덱싱합니다.
- **직접 참조**: LLM이 문서의 특정 페이지나 섹션을 직접 '읽고' 필요한 정보를 추출합니다.
- **정확도 향상**: 벡터 유사도 검색에서 발생하는 '맥락 유실' 문제를 해결하고, 고도로 복잡한 질문에 대해 문서 전체를 조망하는 답변이 가능합니다.

## 3. 주요 특징 및 장점
- **오픈소스 및 유연성**: 다양한 LLM(OpenAI, Anthropic 등)과 연동 가능.
- **인프라 간소화**: 대규모 벡터 DB를 유지관리할 필요가 없어 시스템 복잡도가 낮음.
- **높은 신뢰성**: 모델이 답변의 근거가 되는 문서 위치를 정확히 명시할 수 있음.
- **다양한 포맷 지원**: PDF, HTML 등 복잡한 문서 구조를 가진 정형/비정형 데이터 처리에 강점.

## 5. 상위 시스템으로의 진화: OpenKB와 지속적 위키 컴파일
PageIndex는 단순 검색 프레임워크를 넘어, 안드레이 카파시의 지속적 위키 비전인 **OpenKB**의 핵심 추론 엔진으로 통합되었습니다.
- 문서들을 상호 연결된 위키로 컴파일하고, 각 문서를 계층형 트리로 인덱싱하여 다단계 복합 질의를 해결합니다.
- 위키 지식으로부터 에이전트 스킬(`SKILL.md`)을 증류하는 **Skill Factory**와 연계되어 에이전트 역량 강화로 이어집니다.

## 관련 문서
- [[wiki/RAG/000_RAG-MOC.md|RAG MOC]]
- [[wiki/RAG/OpenKB-Persistent-Wiki-Compiler.md|OpenKB 지속적 위키 컴파일러]]
- [[wiki/RAG/GraphRAG.md|GraphRAG 분석]]
- [[wiki/Models/Reasoning-and-Cognition/000_Reasoning-and-Cognition-MOC.md|추론 및 인지 MOC]]
