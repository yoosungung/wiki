---
title: "로컬 저장소 분석 및 그래프 탐색 도구 (Local Repo Intelligence)"
tags: ["Engineering", "Tools", "Graph-based-Exploration", "Local-LLM"]
last_updated: "2024-05-22"
updated: "2024-05-22"
---

# 로컬 저장소 분석 및 그래프 탐색 도구 개요

코드베이스의 규모가 커짐에 따라 단순 텍스트 검색만으로는 전체 구조와 의존성을 파악하기 어렵습니다. 이를 해결하기 위해 로컬 환경에 설치하여 코드의 '의미적 지도'를 그려주는 도구들이 필수적입니다.

## 1. 핵심 기술: 그래프 기반 탐색 (Graph-based Exploration)
단순 파일 읽기를 넘어 코드 간의 입체적 관계를 파악하는 기술입니다.

- **코드 인덱싱**: 전체 코드를 벡터화하여 의미적 검색(Semantic Search) 지원.
- **심볼 그래프 (AST)**: 함수, 클래스 간의 호출 및 상속 관계를 지도로 생성.
- **자동 탐색 (Traversal)**: 에이전트가 의존성을 따라 관련 파일을 연쇄적으로 분석.

## 2. 주요 로컬 도구 리스트

| 도구명 | 특징 | 설치 및 실행 |
| :--- | :--- | :--- |
| **Bloop** | Rust 기반 고성능 검색 엔진, 시각적 코드 지도 제공. | 데스크탑 앱 또는 오픈소스 빌드 |
| **Aider** | CLI 기반 에이전트 도구, 'Repo Map' 생성에 탁력. | `pip install aider-chat` |
| **Continue** | IDE(VS Code/JetBrains) 통합 로컬 인덱싱 확장 프로그램. | IDE 마켓플레이스 설치 |
| **Tabby** | 자가 호스팅(Self-hosted) 가능한 Copilot 대체제. | Docker 설치 지원 |
| **Sourcegraph** | 엔터프라이즈급 정밀 인덱싱(LSIF) 및 대규모 탐색 지원. | Docker/K8s Self-managed |

## 3. Semantic Layer와의 시너지
이 도구들은 사용자가 정의한 **Semantic Layer**의 구성을 자동화하는 데 기여합니다.

1. **테이블 정의 자동 추출**: DDL과 Foreign Key 관계를 탐색하여 `tables.yaml` 초안 생성.
2. **비즈니스 로직 분석**: SQL View나 프로시저 내의 계산식을 분석하여 `metrics.yaml` 정의에 활용.
3. **데이터 가드레일 강화**: 소스 코드 내의 권한 로직을 분석하여 `role` 기반 접근 제어 설정 참고.

## 🔗 관련 문서
- [[wiki/Agents/Text-to-SQL/Semantic-Layer]]
- [[wiki/Engineering/Data-and-Security/Semantic-Layer-Spec]]
