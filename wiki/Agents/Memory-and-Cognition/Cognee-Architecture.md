---
title: "Cognee - AI Memory System 아키텍처"
related_raw: ["[[wiki/Agents/Memory-and-Cognition/Cognee - AI Memory System.md]]", "[[wiki/Agents/Memory-and-Cognition/Cognee.md]]"]
tags: ['wiki', 'agents', 'memory', 'architecture', 'graphrag']
type: "wiki"
status: "published"
last_updated: "2026-04-20"
---

# Cognee 아키텍처

Cognee는 LLM의 비상태성(Statelessness) 문제를 해결하기 위해 데이터를 지능적이고 검색 가능한 AI 메모리로 변환하는 시스템입니다. 기존의 단순 RAG 시스템을 대체하여 보다 정교한 메모리 계층을 제공합니다.

## 1. 이중 저장 및 하이브리드 아키텍처
Cognee는 의미론적 검색과 구조적 추론을 동시에 지원하기 위해 세 가지 상호 보완적인 저장 시스템을 결합합니다:
- **관계형 저장소 (Relational Storage)**: 문서, 청크(Chunk), 데이터의 출처(Provenance)를 추적합니다.
- **벡터 저장소 (Vector Database)**: 임베딩을 저장하여 의미론적 유사성 검색을 수행합니다.
- **그래프 저장소 (Graph Database)**: 지식 그래프를 통해 엔티티 간의 복잡한 관계를 캡처합니다.

## 2. ECL 파이프라인 (Extract, Cognify, Load)
기존 RAG의 한계를 극복하기 위해 Cognee는 ECL 파이프라인을 제안합니다:
- **Extract (추출)**: 다양한 데이터 소스에서 정보를 가져옵니다.
- **Cognify (인지화)**: 데이터를 청크로 분할하고, 엔티티를 추출하며, 관계를 설정하여 지식 그래프를 구축합니다.
- **Load (로드)**: 처리된 데이터를 저장소에 적재하여 쿼리 가능하게 만듭니다.

## 3. 배포 및 운영 모드
- **Cognee Open Source**: 로컬 데이터베이스(SQLite, LanceDB, Kuzu)를 사용하여 모든 데이터를 로컬에 유지하며 고도의 사용자 정의를 지원합니다.
- **Cognee Cloud**: 관리형 인프라, 웹 UI 대시보드, 리소스 분석 및 보안 기능을 제공하는 엔터프라이즈급 솔루션입니다.

## 관련 문서
- [[wiki/Agents/Memory-and-Cognition/Cognee-Core-Concepts.md|Cognee 핵심 개념]]
- [[wiki/Agents/Memory-and-Cognition/Cognee-Setup-Guide.md|Cognee 설정 가이드]]
- [[wiki/Agents/Memory-and-Cognition/Cognee-MOC.md|Cognee-MOC]]
