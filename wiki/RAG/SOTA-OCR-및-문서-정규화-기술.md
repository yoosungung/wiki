---
related_raw: ["[[2026-06-25-Baidu_Unlimited_OCR_R-SWA_and_SOTA_OCR.md]]"]
tags: ["#wiki", "OCR", "Unlimited-OCR", "R-SWA", "Agentic-RAG", "Data-Normalization"]
---

# SOTA OCR 모델 및 에이전트 RAG 문서 정규화

비정형 기업 문서(스캔 PDF, 이미지 등)를 기계 가독성 및 시맨틱 보존율이 높은 표준 마크다운(Markdown) 포맷으로 변환하는 **OCR 및 문서 정규화 기술**은 현대 에이전틱 RAG(Agentic RAG)의 핵심 전처리 레이어입니다. AI 에이전트는 구조화된 마크다운 데이터에서 오류 없이 정확하게 도구를 호출하고 정보를 파싱합니다.

## 1. 최신 OCR 기술 동향
- **Baidu Unlimited OCR**: DeepSeek OCR을 기반으로 학습된 3B 규모의 모델로, **R-SWA (Reference Sliding Window Attention)** 기법을 최초로 도입했습니다. 이를 통해 페이지 한계를 넘어선 초장문 및 복잡한 레이아웃의 문서를 소실 없이 정확하게 텍스트로 복원해 냅니다.
- **Mistral OCR 4**: 상용 고성능 문서 레이아웃 분석 및 문자 추출 API로, 고정밀 표(Table) 파싱과 다국어 처리에 강점을 가집니다.
- **Chandra 2 (Datalab)**: 오픈소스 SOTA 라인업으로, 셀프 호스팅 및 API 활용이 용이하여 기업 내부 데이터의 프라이버시를 지키면서 고속 정규화 처리가 가능합니다.

## 2. 평가 벤치마크
OCR 모델의 성능을 객관적으로 판별하기 위해 다음과 같은 현대적 벤치마크셋이 활용됩니다:
1. **OlmOCRBench (AI2)**: 대규모 복합 레이아웃 및 폰트 인식 성능을 측정하는 벤치마크.
2. **OmniDocBench (Shanghai AI Lab)**: 논문, 특허, 사업 계획서 등 구조 분석 능력을 다각도로 검증하는 표준 벤치마크.

## 🔗 연결된 문서
- [[wiki/RAG/OpenDataLoader-PDF-Parser.md]] — PDF 내 Bounding Box 좌표 및 구조 추출 라이브러리.
- [[wiki/RAG/omniparse-멀티포맷-데이터-정규화-파이프라인.md]] — 오디오, 비디오, 스캔 문서를 일괄 가공해 주는 omniparse 기술.
