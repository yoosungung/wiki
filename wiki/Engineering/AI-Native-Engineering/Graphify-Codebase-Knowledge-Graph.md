---
title: "Graphify: 코드베이스 지식 그래프(Knowledge Graph) 구축 도구"
related_raw: ["[[Codebase Knowledge Graph with Graphify | AI Engineering님이 토픽에 대해 올림 | LinkedIn.md]]"]
tags: ["Engineering", "AI-Native", "Codebase", "Knowledge_Graph", "Graphify", "RAG"]
type: "wiki"
status: "published"
last_updated: "2026-05-15"
updated: "2026-05-15"
---

# Graphify: 코드를 데이터가 아닌 '지식'으로 보는 방법

## 1. 개요
Graphify는 복잡한 소프트웨어 코드베이스를 분석하여 함수, 클래스, 모듈 간의 관계를 **지식 그래프(Knowledge Graph)** 형태로 시각화하고 인덱싱하는 도구입니다. 이를 통해 AI 에이전트가 코드의 맥락을 훨씬 더 깊이 있게 이해할 수 있도록 돕습니다.

## 2. 핵심 기능
- **자동 그래프 생성**: 소스 코드를 스캔하여 호출 그래프(Call Graph), 의존성 맵, 상속 구조를 그래프 DB 형식으로 변환합니다.
- **시맨틱 링크**: 단순한 텍스트 유사도가 아닌, 코드의 논리적 연결 관계를 바탕으로 검색(Retrieval)이 가능하게 합니다.
- **에이전트 친화적 인터페이스**: Claude Code나 Cursor와 같은 에이전트가 전체 시스템 아키텍처를 조망하며 수정 범위를 결정할 수 있는 '지도' 역할을 합니다.

## 3. 도입 효과
- **맥락 유실 방지**: 특정 함수 수정 시 영향이 가는 다른 모듈을 즉각적으로 파악하여 에러 발생률을 낮춥니다.
- **효율적 코드 검색**: "이 기능을 담당하는 핵심 로직이 어디에 분포해 있어?"와 같은 추상적인 질문에 대해 정확한 엔티티 묶음을 반환합니다.
- **RAG 고도화**: 일반적인 텍스트 기반 RAG보다 코드의 구조적 특성을 잘 반영한 정밀 검색이 가능합니다.

## 4. 활용 시나리오
- **대규모 마이그레이션**: 서비스 전체의 의존성을 파악해야 하는 리팩토링 작업.
- **신규 입사자 온보딩**: 코드베이스의 전체 구조를 시각적으로 탐색하며 학습.
- **자율형 코딩 에이전트 연동**: 에이전트에게 코드의 논리적 지도를 제공하여 작업 지능 향상.

## 관련 문서
- [[wiki/Engineering/AI-Native-Engineering/000_AI-Native-Engineering-MOC.md|AI-Native Engineering MOC]]
- [[wiki/RAG/GraphRAG.md|GraphRAG 분석]]
- [[wiki/Engineering/Local-Repo-Intelligence.md|로컬 레포지토리 인텔리전스]]
