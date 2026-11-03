---
title: "Cognee - AI Memory System 아키텍처"
related_raw: ["[[wiki/Agents/Memory-and-Cognition/Cognee - AI Memory System.md]]", "[[wiki/Agents/Memory-and-Cognition/Cognee.md]]", "[[2026-11-03-Cognee-GLiNER-Local-Knowledge-Graph-Extraction.md]]"]
tags: ['wiki', 'agents', 'memory', 'architecture', 'graphrag', 'GLiNER', 'Local-First', 'ExactRoute']
type: "wiki"
status: "published"
last_updated: "2026-11-03"
updated: "2026-11-03"
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
- **Cognee Open Source**: 로컬 데이터베이스(SQLite, LanceDB, Kuzu / Ladybug)를 사용하여 모든 데이터를 로컬에 유지하며 고도의 사용자 정의를 지원합니다.
- **Cognee Cloud**: 관리형 인프라, 웹 UI 대시보드, 리소스 분석 및 보안 기능을 제공하는 엔터프라이즈급 솔루션입니다.

## 4. GLiNER 통합 기반 100% 로컬 무-LLM(Zero-Hosted-LLM) 지식 그래프 구축
데이터베이스(SQLite, LanceDB)가 로컬에 있더라도, 지식 그래프 구축(Cognify) 단계에서 원본 대화나 비정형 텍스트를 외부 호스팅 LLM API로 전송해 엔티티를 추출한다면 전체 메모리 파이프라인은 진정한 로컬·프라이버시 보존 시스템이 아닙니다.
- **GLiNER + fastembed 로컬 추출 파이프라인**:
  1. **GLiNER**([[wiki/Models/Optimization-and-Serving/GLiNER2.5-Decide-Structured-Decision-Encoder.md|GLiNER 계열 인코더]])가 순차적 텍스트 생성이나 외부 LLM 호출 없이 로컬에서 비정형 텍스트의 엔티티(Entities)와 관계(Relationships)를 즉시 추출합니다.
  2. **fastembed**가 CPU 상에서 고속으로 벡터 임베딩을 생성합니다.
  3. **SQLite + LanceDB + Ladybug**가 그래프·벡터·메타데이터를 100% 로컬 머신에 저장합니다.
- **필드 단위 오프로딩 패턴 (ExactRoute 연동)**: 로깅된 기존 LLM 호출을 필드별로 분석하여 단순 조회(Lookup), 규칙(Rules), GLiNER 같은 소형 NER 인코더나 분류기로 처리 가능한 부분을 자체 데이터 정확도 검증 후 로컬로 오프로딩하고, 꼭 필요한 추론만 LLM으로 라우팅하여 비용과 데이터 유출을 최소화합니다.

## 관련 문서
- [[wiki/Agents/Memory-and-Cognition/Cognee-Core-Concepts.md|Cognee 핵심 개념]]
- [[wiki/Agents/Memory-and-Cognition/Cognee-Setup-Guide.md|Cognee 설정 가이드]]
- [[wiki/Agents/Memory-and-Cognition/Cognee-MOC.md|Cognee-MOC]]
- [[wiki/Models/Optimization-and-Serving/GLiNER2.5-Decide-Structured-Decision-Encoder.md|GLiNER2.5-Decide 구조화 결정 인코더]]
- [[wiki/Agents/Memory-and-Cognition/RAW-RAG-Raw-History-Retrieval-Baseline.md|RAW-RAG 원본 기록 리랭킹 베이스라인]]
