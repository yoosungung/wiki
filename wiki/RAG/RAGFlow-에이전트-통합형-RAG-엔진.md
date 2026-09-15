---
title: "RAGFlow: 에이전트 워크플로우 통합형 엔터프라이즈 RAG 엔진"
last_updated: "2026-07-28"
updated: "2026-07-28"
related_raw: ["[[raw/2026-07-28-ragflow_open_source_rag_engine_with_agentic_capabilities.md]]"]
tags: [RAG, Agent-Workflow, Document-Parsing, InfiniFlow, Enterprise]
---

# RAGFlow: 에이전트 워크플로우 통합형 엔터프라이즈 RAG 엔진

이 문서는 InfiniFlow가 개발한 오픈소스 RAG(Retrieval-Augmented Generation) 엔진인 **RAGFlow**의 아키텍처 및 에이전트 통합 특징을 분석합니다.

---

## 1. 개요

**RAGFlow**는 단순한 텍스트 임베딩 및 검색 수준의 RAG를 넘어, 대규모 비정형 문서의 **레이아웃 분석 및 의미적 파싱(Deep Document Understanding)**과 **에이전트 워크플로우(Agentic Workflow)**를 유기적으로 융합한 엔터프라이즈급 오픈소스 RAG 엔진입니다. 복잡한 표, 이미지, 수식이 섞인 문서에서 의미적 왜곡 없이 고정밀 컨텍스트 레이어를 LLM에 제공하는 것을 목표로 합니다.

---

## 2. 주요 아키텍처 및 기술 특징

### 2.1. 깊은 문서 이해 (Deep Document Understanding) 기반 파싱
- **레이아웃 보존**: PDF, Word, PPT 등 다양한 비정형 문서의 폰트, 표(Table), 캡션, 헤더 등의 기하학적 구조를 인공지능 기반 레이아웃 파서로 정밀하게 해독합니다.
- **의미적 청킹 (Semantic Chunking)**: 단순히 글자 수 기준으로 자르는 것이 아니라, 문맥의 단락과 구조적 단위를 기반으로 유의미한 의미 청크를 형성하여 검색 정확도를 극대화합니다.

### 2.2. RAG와 에이전트의 결합 (RAG + Agentic Capabilities)
RAGFlow는 단순 검색 후 LLM 주입 구조에서 탈피하여, 에이전트가 검색 프로세스 자체를 직접 통제할 수 있는 **지능형 컨텍스트 레이어**를 내장합니다.
- **다단계 검색 의사결정**: 에이전트가 사용자의 질문을 분석해 추가 검색이 필요한지 여부, RAGDB 쿼리 파라미터 튜닝, 검색 결과의 상호 충돌 검증 등을 자율적으로 판단하여 지식 추론의 깊이를 확장합니다.

```text
                  RAGFlow 에이전틱 워크플로우
                  ===========================
                  
   [사용자 질의] ──> [RAGFlow Agent] ──(자율 쿼리 튜닝)──> [Deep Document 파서]
                          │                                        │
                          ▼                                        ▼
   [최종 가설/답변] <── (지식 융합 및 추론) <──── (정밀 청크 추출 및 캐싱)
```

---

## 3. 실전 구축 및 배포 가이드

RAGFlow는 도커(Docker) 기반으로 신속하게 배포 및 검증할 수 있습니다.

### 3.1. Docker Compose 기반 배포
```bash
# 1. RAGFlow 저장소 복제 및 폴더 진입
git clone https://github.com/infiniflow/ragflow.git
cd ragflow

# 2. Docker 이미지 다운로드 및 가동 (기본 포트: 80)
docker compose -f docker/docker-compose.yml up -d
```

서버가 실행되면 웹 브라우저를 통해 데스크톱 대시보드(기본 주소: `http://localhost`)에 접근하여 문서 업로드, 청킹 프리뷰 설정 및 에이전트 룰셋을 정의할 수 있습니다.

---

## 🔗 관련 문서 링크
- 비정형 OCR 및 데이터 파싱: [[wiki/RAG/SOTA-OCR-및-문서-정규화-기술.md]]
- RAG 파이프라인 실패 요인 분석: [[wiki/RAG/프로덕션-RAG-파이프라인-실패-요인-및-해결-방안.md]]
- [[wiki/RAG/000_RAG-MOC.md]]
- [[index.md]]
