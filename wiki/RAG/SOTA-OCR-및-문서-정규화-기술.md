---
related_raw: ["[[2026-06-25-Baidu_Unlimited_OCR_R-SWA_and_SOTA_OCR.md]]", "[[2026-07-31-allenai-olmocr-pdf-linearization-toolkit.md]]", "[[2026-11-03-Unlimited-OCR-2-MiniCPM-OCR-Jev-Verifier.md]]"]
tags: ["#wiki", "OCR", "Unlimited-OCR-2", "SR-SWA", "MiniCPM-OCR", "JevOCRBench", "TackleVision", "Agentic-RAG", "Data-Normalization"]
last_updated: "2026-11-03"
updated: "2026-11-03"
---

# SOTA OCR 모델 및 에이전트 RAG 문서 정규화

비정형 기업 문서(스캔 PDF, 이미지, 300페이지 계약서 등)를 기계 가독성 및 시맨틱 보존율이 높은 표준 마크다운(Markdown) 포맷으로 변환하는 **OCR 및 문서 정규화 기술**은 현대 에이전틱 RAG(Agentic RAG)의 핵심 전처리 레이어입니다. RAG 파이프라인에서 그라운딩(Grounding)이 조용히 깨지는 가장 흔한 원인은 병합된 표 셀(Merged cell)이나 페이지 경계를 넘어가는 테이블 헤더의 오독이므로, **초장문 문맥 유지 OCR**과 **경량 추출 검증기(OCR Goalkeeper)**의 결합이 필수적입니다.

## 1. 최신 OCR 기술 동향 및 오픈소스 라인업
- **Baidu Unlimited OCR & Unlimited OCR 2**:
  - 1세대(3B)가 R-SWA를 도입한 데 이어, 오픈소스로 공개된 **Unlimited OCR 2**는 **SR-SWA (Sparse Reference Sliding Window Attention)**와 **무제한 호라이즌 디코딩(Unlimited-Horizon Decoding)** 및 적극적인 KV 캐시 축출(Eviction)을 결합했습니다.
  - 이를 통해 **300페이지 분량의 장문 계약서·규제 문서**를 컨텍스트 고갈 없이 연속으로 읽어내며, 기존 Full Attention 대비 **7배 빠른 추론 속도(7x faster)**를 달성했습니다.
- **OpenBMB MiniCPM-OCR 스위트 (1.0 추출기 + Jev 검증기 이중 구조)**:
  - **MiniCPM-OCR 1.0 (1B/1.3B)**: GPU 클러스터 없이 온디바이스·단일 노드에서 구동되는 초경량 모델로 `Real5-OmniDocBench`에서 **93.68점(SOTA)**을 기록했습니다.
  - **MiniCPM-OCR Jev (2B OCR Goalkeeper)**: 추출기 모델에 종속되지 않는(Model-agnostic) **2B 파라미터 OCR 사후 검증기**입니다. `JevOCRBench`에서 **93.6점**을 기록해 397B 초대형 모델에 필적하는 검수 정확도를 보이며, `DSpark` 투기적 디코딩 결합 시 **분당 128페이지(128 pages/min)**의 초고속 처리량을 달성합니다(`vLLM`, `SGLang`, `llama.cpp` 양자화 및 파인튜닝 지원). 거대 리트리버에 연산을 쓰는 것보다 2B OCR 검증기로 표 헤더·병합 셀 추출 오류를 먼저 잡아내는 것이 RAG 정확도에 훨씬 높은 ROI를 제공합니다.
- **Liquid AI LFM3 OCR**: 비-트랜스포머 유체 파운데이션 모델(LFM) 기반의 저지연 문서 인식 라인업입니다.
- **olmocr (AI2) 및 TackleVision 독립 검증**:
  - AI2의 `olmOCR`은 VLM 기반 오픈소스 PDF 선형화 툴킷이며, 공식 벤치마크인 **`olmOCR-bench` (1,403페이지, 8,413개 테스트)**는 상용 벤더들의 자체 발표치(실제 독립 테스트 대비 10~15점 부풀려지는 경향)를 검증하는 표준 척도입니다.
  - 독립 재현 검증(2회 from-scratch 실행)에서 **TackleVision**이 **86.1점**을 기록해 독립 검증된 시스템 중 최고점을 달성했으며, 특히 고밀도 세칙 문서(EOBs, 법원 소송 기록 **+10.3점**), 구형 팩스 스캔본(**+9.2점**), 청구서·검사 결과 표(**+6.9점**)에서 큰 격차를 입증했습니다.
- **Mistral OCR 4 & Chandra 2 (Datalab)**: 고정밀 테이블 파싱 및 프라이버시 보존 셀프 호스팅을 지원하는 상용·오픈소스 라인업입니다.

## 2. 평가 벤치마크
OCR 및 문서 검증 모델의 성능을 객관적으로 판별하기 위해 다음 3대 벤치마크가 활용됩니다:
1. **olmOCR-bench (AllenAI)**: 1,403페이지·8,413개 실전 테스트로 구성된 독립 재현성 검증 표준 벤치마크.
2. **Real5-OmniDocBench / OmniDocBench (Shanghai AI Lab)**: 논문, 특허, 사업 계획서, 실전 스캔본 등 복합 레이아웃 구조 분석 능력을 검증하는 벤치마크.
3. **JevOCRBench**: OCR 추출 결과물의 오류·누락·표 왜곡을 판별하는 검증기(Verifier/Goalkeeper) 전용 벤치마크.

## 🔗 연결된 문서
- [[wiki/RAG/Dual-Interface-Document-Extraction-CLI-and-MCP.md]] — 배치 CLI와 에이전트 런타임 MCP 이중 문서 추출 파이프라인.
- [[wiki/Agents/Evaluations/JevAdvBench-Decision-Model-Adversarial-Benchmark.md]] — 결정 모델 및 벤치마크 재현성 감사.
- [[wiki/RAG/olmocr-pdf-linearization-toolkit.md]] — AI2의 VLM 기반 PDF-to-Text 데이터 선형화 오픈소스.
- [[wiki/RAG/OpenDataLoader-PDF-Parser.md]] — PDF 내 Bounding Box 좌표 및 구조 추출 라이브러리.
- [[wiki/RAG/omniparse-멀티포맷-데이터-정규화-파이프라인.md]] — 오디오, 비디오, 스캔 문서를 일괄 가공해 주는 omniparse 기술.
