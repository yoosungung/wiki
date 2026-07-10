# OSI 표준 기반 도메인 간 맥락 공유 기법

## 1. 연구 개요
- **연구 목적**: 시맨틱 레이어 표준(OSI)을 활용하여 도메인이 다른 에이전트 간의 데이터 분석 맥락을 공유하는 기법 연구
- **우선순위**: High

## 2. 주요 연구 내용
- **OSI(Open Semantic Interface) 표준 분석**: ThoughtSpot, Snowflake, Denodo 등이 주도하는 벤더 중립적 시맨틱 모델 표준 명세 분석.
- **에이전트 간 맥락 공유**: 서로 다른 도메인 에이전트가 동일한 데이터 엔터티를 동일한 비즈니스 로직(Metrics, Rules)으로 이해하게 하는 상호운용성 확보.
- **MCP(Model Context Protocol) 연동**: OSI 표준으로 정의된 시맨틱 컨텍스트를 MCP 서버를 통해 여러 에이전트에게 실시간 배포하는 아키텍처 설계.

## 3. 핵심 기술 요소
- **Semantic Mapping**: 물리적 스키마 ↔ OSI 표준 모델 ↔ 에이전트 인지 모델 간의 매핑 기술.
- **Context Propagation**: 분석 과정에서 생성된 중간 맥락(Intermediate Context)을 OSI 형식으로 직렬화하여 타 에이전트에 전이.

## 🔍 탐색 매개변수 (Exploration Parameters)
- **Primary Keywords**: `Open Semantic Interface (OSI) Specification`, `Agentic Semantic Modeling`, `Semantic Layer Interoperability`
- **Secondary Keywords**: `ThoughtSpot OSI`, `Snowflake Semantic Layer Integration`, `MCP Semantic Context Sharing`
- **Channels**: `arXiv`, `Google Scholar`, `Snowflake Engineering Blog`, `ThoughtSpot Developers`
- **Focus**: 시맨틱 레이어의 벤더 중립적 표준화 및 에이전트 간 맥락 전이 기술의 최신 논문(2024-2026) 탐색.

## 3. 진행 상태
- **초기 기획 및 기술 조사 완료 (2026-04-22)**: 
    - OSI v1.0 사양(2026.1.27 발표) 확인 완료.
    - YAML 기반의 Datasets, Metrics, Contexts 구조 분석.
    - Snowflake와 ThoughtSpot 간의 실제 연동 사례(Cortex Analyst, Spotter) 확인.
    - 차기 단계: OSI 기반의 MCP 서버 프로토타입 설계 및 맥락 전이 시나리오 구체화.

