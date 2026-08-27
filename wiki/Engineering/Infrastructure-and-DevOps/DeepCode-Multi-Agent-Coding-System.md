---
tags:
  - inbox
type: wiki
status: published
---

# DeepCode Multi Agent Coding System

HKUDS에서 공개한 **DeepCode**는 세 가지 각기 다른 형태의 입력을 받아 프로덕션 수준의 작동하는 코드를 자동 생성해 주는 오픈소스 멀티 에이전트 코딩 시스템입니다.

## 기본 제공 3가지 모드
1.  **Paper2Code**: 연구 논문을 입력하면 방법론을 읽고, 레퍼런스 구현을 발굴한 뒤 알고리즘을 코드로 재현합니다.
2.  **Text2Web**: 일반 텍스트 설명을 기반으로 완전한 프론트엔드 애플리케이션을 구축합니다.
3.  **Text2Backend**: 요구사항이 담긴 URL 또는 텍스트를 통해 확장 가능한 백엔드 코드를 생성합니다.

## 시스템 파이프라인 아키텍처
DeepCode는 아래의 4가지 주요 에이전트가 조화롭게 작동하는 파이프라인을 갖추고 있습니다.
*   **Planner (계획자)**: 입력을 분석하여 구조화된 구현 로드맵으로 분해합니다.
*   **Reference Mining Agent (참조 마이닝)**: 관련 코드 패턴과 레퍼런스 저장소를 발굴합니다.
*   **Code Generation Agent (코드 생성)**: 모든 정보를 종합하여 코드를 합성하고 테스트를 수행합니다.
*   **Orchestrator (오케스트레이터)**: 입력의 복잡도에 따라 전체 에이전트들의 워크플로우를 조정하고 조율합니다.

CLI, Web UI, Docker를 통한 즉시 배포를 지원하며, OpenAI, Anthropic, Gemini 등 OpenAI 호환 엔드포인트를 제공하는 대부분의 모델과 연동할 수 있습니다.
