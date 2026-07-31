---
title: "olmocr: AI2의 PDF-to-Text 데이터 정규화 툴킷"
date: "2026-07-31"
last_updated: "2026-07-31"
updated: "2026-07-31"
related_raw: ["[[2026-07-31-allenai-olmocr-pdf-linearization-toolkit.md]]"]
tags: ["RAG", "OCR", "PDF-Linearization", "Data-Normalization"]
type: "wiki"
---

# olmocr: AI2의 PDF-to-Text 데이터 정규화 툴킷

[olmocr](https://github.com/allenai/olmocr)은 Allen Institute for AI (Ai2)에서 개발한 오픈소스 PDF-to-Text 정규화 툴킷입니다. 대규모 언어 모델(LLM) 학습 및 RAG 파이프라인에서 비정형 PDF 문서를 자연스러운 읽기 순서(Reading Order)와 구조화된 정보(표, 리스트, 수식 등)를 보존한 채 마크다운 형식으로 선형화(Linearization)하는 데 특화되어 있습니다.

## 1. 주요 특징 및 아키텍처

- **VLM 기반의 레이아웃 이해**: 단순 텍스트 추출 엔진의 한계를 극복하기 위해, 시각언어모델(Vision-Language Model)인 **olmOCR-2-7B-1025**를 활용하여 문서의 레이아웃, 표, 컬럼 순서를 시각적으로 파악하고 정형화된 마크다운을 출력합니다.
- **대규모 분산 처리 지원**: 수백만 페이지 분량의 PDF 문서를 병렬 처리할 수 있도록 설계되었으며, AWS S3 버킷 및 분산 노드/클러스터 연동을 기본 지원합니다.
- **구조적 보존**: 본문 내 수학 공식(LaTeX 인코딩), 중첩 리스트, 병렬 구조의 테이블 등을 파싱 에러 없이 정확하게 텍스트화합니다.

## 2. 설치 및 실행 예시

### 1) 패키지 설치
```bash
pip install olmocr
```

### 2) CLI 기반 PDF 선형화 실행
```bash
# 단일 PDF 파일을 마크다운 파일로 변환
olmocr parse --input document.pdf --output document.md --model allenai/olmOCR-2-7B-1025
```

## 3. RAG 파이프라인에서의 활용 및 의의

전통적인 PDF 파서(예: PyPDF, PDFMiner)는 2단 편집(Two-column) 레이아웃이나 복잡한 표를 처리할 때 줄 바꿈 및 텍스트 순서가 꼬이는 고질적인 한계를 가집니다. olmocr은 VLM의 시각적 컨텍스트 이해력을 전처리 단계에 결합하여 이 문제를 완벽히 방어함으로써, 검색 증강 생성(RAG)의 검색 정확도와 에이전트 도구 호출 성능을 크게 증대시킵니다.

## 🔗 연결된 문서
- [[wiki/RAG/SOTA-OCR-및-문서-정규화-기술.md]]
- [[wiki/RAG/OpenDataLoader-PDF-Parser.md]]
- [[wiki/RAG/omniparse-멀티포맷-데이터-정규화-파이프라인.md]]
