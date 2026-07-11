---
title: RAG-Anything Multimodal Document Processing Framework
status: published
tags: [RAG, Multimodal, KnowledgeGraph, GraphRAG]
related_raw: ["[[2026-05-08-rag-anything-multimodal.md]]"]
last_updated: 2026-05-08
updated: "2026-05-08"
---

# RAG-Anything: Multimodal Document Processing Framework

RAG-Anything은 텍스트, 이미지, 표, 수식, 차트 등 다양한 형태의 데이터를 단일 통합 파이프라인에서 처리하고 검색할 수 있는 포괄적인 [[wiki/RAG/000_RAG-MOC.md|RAG]] 프레임워크입니다.

## 🚀 주요 기능 및 아키텍처

### 1. 범용 문서 지원 (Universal Document Support)
- **지원 포맷**: PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX 및 이미지 파일.
- **특화 프로세서**: 이미지, 표, 수학 공식, 사용자 정의 콘텐츠 유형을 위한 전용 처리기 포함.

### 2. 멀티모달 지식 그래프 (Multimodal Knowledge Graph)
- 자동 엔티티 추출 및 모달리티 간 관계 발견을 통해 단순 벡터 검색을 넘어서는 구조적 지식을 형성합니다.
- [[wiki/RAG/GraphRAG.md|GraphRAG]]와 유사하게 그래프 탐색을 활용한 하이브리드 검색을 지원합니다.

### 3. 하이브리드 검색 (Hybrid Retrieval)
- **벡터 유사도 검색**: 의미론적 유사성 기반 검색.
- **그래프 탐색 (Graph Traversal)**: 지식 그래프의 연결성을 활용한 정교한 문맥 파악.

### 4. VLM 강화 쿼리 (VLM-Enhanced Query)
- 검색된 컨텍스트에 이미지가 포함된 경우, 비전 언어 모델(VLM)이 자동으로 해당 이미지를 분석하여 더 깊은 인사이트를 제공합니다.

## 🛠️ 기술 스택 및 설치
- **파서 옵션**: MinerU, Docling, PaddleOCR 중 선택 가능.
- **설치**: `pip install raganything`
- **저장소**: [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything)

## 🔗 관련 문서
- [[wiki/RAG/000_RAG-MOC.md]]
- [[wiki/RAG/GraphRAG.md]]
- [[wiki/Models/Multimodal-and-Vision/000_Multimodal-MOC.md]]
