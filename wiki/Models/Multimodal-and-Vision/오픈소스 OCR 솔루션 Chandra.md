---
title: "오픈소스 OCR 솔루션 Chandra"
related_raw: ["[[wiki/Models/Multimodal-and-Vision/오픈소스 OCR 솔루션 Chandra.md]]"]
tags: ['wiki', 'agents_and_systems', 'llm_agent_&_deep_agents', 'tools']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

# 2025년 최고의 오픈소스 OCR 솔루션: Chandra

이 LinkedIn 게시물은 2025년 최고의 오픈소스 OCR 솔루션으로 'Chandra'를 추천하는 내용입니다. 게시자는 RAG 및 Agentic 시스템의 데이터 처리 개발을 위해 다양한 오픈소스 및 상용 OCR/문서 분석 솔루션을 테스트했으며, 그 중 Chandra가 가장 뛰어난 성능을 보였다고 언급합니다.

## 주요 특징

1.  **다양한 레이아웃 블록 인식**: 표, 수식, 이미지, 캡션, 각주 등 15가지 레이아웃 블록을 인식하고 각각의 바운딩 박스 좌표까지 추출합니다.
2.  **특수 요소 인식**: 손으로 쓴 메모, 체크박스, 서명까지 인식하여 오래된 레거시 문서나 스캔된 양식 디지털화에 유용합니다.
3.  **다양한 출력 형식**: Markdown, HTML, JSON 중 선택 가능하며, LLM 파이프라인에 바로 연결할 수 있습니다. JSON 출력은 각 블록별 좌표와 텍스트를 구조화하여 제공합니다.
4.  **다국어 지원**: 한국어, 영어, 일본어, 중국어 등 40개 이상의 언어를 문제없이 처리합니다.
5.  **유연한 배포**: 로컬 GPU(HuggingFace)로 직접 실행하거나, 서버에 vLLM을 띄워 API로 호출할 수 있습니다.

## 기술적 특징

Chandra는 Vision-Language Model(VLM) 기반이며, Qwen3 VL을 사용합니다. 이미지를 입력받아 구조화된 HTML을 생성하는 방식으로 문서 이해를 "이미지-텍스트 생성" 문제로 접근하여 복잡한 레이아웃도 자연스럽게 처리합니다.

## 사용법

CLI에서 `chandra input.pdf ./output` 명령어를 사용하거나, Streamlit 기반의 웹 UI를 통해 쉽게 테스트할 수 있습니다. vLLM으로도 제공되어 운영 환경에서도 활용 가능합니다.

게시자는 Agent나 RAG 파이프라인 개발 중 문서 처리 문제로 고민하는 사람들에게, 특히 표, 수식, 손글씨가 포함된 복잡한 문서를 다루는 경우 Chandra를 테스트해볼 것을 강력히 추천합니다.

## 관련 URL

*   개인 정리 자료: [https://lnkd.in/gQPK8HV3](https://lnkd.in/gQPK8HV3)
*   GitHub 저장소: [https://lnkd.in/gc-78wsz](https://lnkd.in/gc-78wsz)

## 관련 노트

*   Areas/RAG기술현황(1)
*   [[wiki/RAG/GraphRAG]]
*   [[wiki/Agents/Frameworks/MCP/AI-에이전트-개발-트렌드-MCP에서-Skills로]]
*   [[wiki/Engineering/Infrastructure-and-DevOps/DGX Spark에서의 VLM 파인튜닝]]
*   [[wiki/Models/Multimodal-and-Vision/DeepSeek-OCR]]

---
*tags*: #OCR, #DocumentAI, #RAG, #VLM, #AIAgent, #LLM, #오픈소스, #문서처리, #VisionLanguageModel*
