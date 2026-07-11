---
title: "Mem0-vs-Cognee-vs-QMD-Comparison"
related_raw: ["[[wiki/Agents/Memory-and-Cognition/Mem0-vs-Cognee-vs-QMD-Comparison.md]]"]
tags: ['wiki', 'knowledge_and_memory', 'advanced_rag_&_knowledge_graph', 'agent_memory_and_cognition']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# AI 메모리 시스템 비교: Mem0 vs Cognee vs QMD

### 1. 개요 및 핵심 컨셉
LLM 에이전트가 장기적인 맥락을 유지하고 지식을 체계적으로 관리하기 위해 사용되는 세 가지 핵심 메모리 프레임워크인 Mem0, Cognee, QMD를 비교 분석합니다. 각 프레임워크는 데이터 저장 방식(벡터, 그래프, 텍스트)과 활용 목적에 따라 뚜렷한 차이를 보입니다.

### 2. 주요 기술 세부 사항
- **Mem0 (Conversational Fact Extraction):** 사용자 대화에서 핵심 사실(Fact)을 추출하여 벡터 데이터베이스에 저장합니다. 사용자별 프로필 관리에 강점이 있으며, '사용자는 파이썬을 좋아한다'와 같은 개인화된 정보를 유지하는 데 최적화되어 있습니다.
- **Cognee (Knowledge Graph Based):** 엔티티 간의 관계를 지식 그래프(Knowledge Graph) 형태로 구축합니다. 복잡한 의존성 추론이 필요한 프로젝트 관리나 코드 분석 등에 강력한 성능을 발휘합니다.
- **QMD (Query Markup Documents):** BM25와 벡터 검색을 하이브리드로 사용하며, 마크다운 문서 구조를 최대한 활용합니다. 토큰 비용이 저렴하고 로컬 검색 품질이 뛰어나 문서 기반 RAG 시스템에 적합합니다.

### 3. 기술 비교 요약
| 기능 | Mem0 | Cognee | QMD |
| :--- | :--- | :--- | :--- |
| **저장 구조** | 벡터 (Flat Fact) | 지식 그래프 | 하이브리드 (Text/Vector) |
| **주요 용도** | 개인 비서, 맞춤형 챗봇 | 복잡한 관계 추론 | 대규모 문서 검색 |
| **비용 효율** | 중간 | 중간 (LLM 기반 그래프 구축) | 매우 높음 |

### 4. 관련 기술 URL 및 리소스
- [Mem0 GitHub Repository](https://github.com/mem0ai/mem0)
- [Cognee Documentation](https://docs.cognee.ai/)
- [QMD Specification](https://example.com/qmd-spec)

### 5. 설명 이미지 추출 (Conceptual)
- ![Memory Framework Comparison](https://example.com/memory-comp.png) (세 가지 프레임워크의 데이터 흐름도 비교)

### 6. 관련 노트 링크
- [[wiki/Agents/Memory-and-Cognition/Mem0]]
- [[wiki/Agents/Memory-and-Cognition/Mem0-vs-Cognee-Comparison-2026]]
- [[wiki/RAG/Knowledge Graph Extraction and Challenges]]
