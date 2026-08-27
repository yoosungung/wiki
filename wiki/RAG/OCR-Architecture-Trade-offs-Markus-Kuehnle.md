# OCR 아키텍처 트레이드오프 (Markus Kuehnle)

## 핵심 주장 (Claims)
단 하나의 "최고의" OCR 접근 방식은 없습니다. 모든 문서 추출 아키텍처는 레이아웃 인식, 지연 시간(latency), 컴퓨팅 비용 간의 타협점입니다.

## 시스템 구조 및 설계 (Architecture & Design)
의료 문서 등에서 구조화된 지식을 안정적으로 추출하기 위한 핵심 문서 추출 기법 7가지는 다음과 같습니다.

1. **정적 바운딩 박스 크롭 (Static Bounding-Box Cropping)**
   - **도구**: AWS Textract (Queries API)
   - **적합**: 고정된 양식 (정부/세금 폼). 매우 빠르고 저렴함.
   - **한계**: 시각적 변형, 크기 조정, 회전에 취약함.

2. **기하학적 앵커 정렬 (Geometric Anchor Alignment)**
   - **도구**: OpenCV
   - **적합**: 물리적 왜곡이 있는 모바일 사진 스캔.
   - **한계**: 벤더마다 레이아웃이 동적으로 다를 경우 실패함.

3. **2단계 탐지 및 인식 (Two-Stage Detection + Recognition)**
   - **도구**: PaddleOCR
   - **적합**: 평면 문서, 영수증, 간판 등의 빠른 GPU 파싱.
   - **한계**: 다중 열 읽기 순서 등 전체적인 레이아웃을 무시함.

4. **다단계 문서 오케스트레이션 (Multi-Stage Document Orchestration)**
   - **도구**: Docling
   - **적합**: 복잡한 PDF 및 연구 논문을 Markdown/JSON으로 변환하는 RAG 파이프라인.
   - **한계**: 높은 지연 시간과 무거운 시스템 의존성.

5. **특수 문서 트랜스포머 (Specialized Document Transformers)**
   - **도구**: LayoutLMv3 / Donut
   - **적합**: 가변적인 송장, 수학 수식, 손글씨 노트의 키-값 추출.
   - **한계**: 높은 GPU 메모리 사용량, 어노테이션 오버헤드, 환각(hallucination) 위험.

6. **제로샷 멀티모달 VLM (Zero-Shot Multimodal VLMs)**
   - **도구**: Qwen2.5-VL
   - **적합**: 사전 훈련 데이터가 없는 비구조화되고 매우 가변적인 문서.
   - **한계**: 높은 API 비용, 지연 시간, 숫자 관련 환각 위험.

7. **동적 다중 엔진 라우팅 (Dynamic Multi-Engine Routing)**
   - **도구**: LlamaIndex Document Agents
   - **적합**: 수백만 장의 혼합된 페이지를 처리하는 엔터프라이즈 파이프라인 (간단한 텍스트는 CPU로, 복잡한 표/손글씨는 Vision-LLM으로 라우팅).
   - **한계**: 높은 아키텍처 복잡성과 스키마 정규화 오버헤드.
