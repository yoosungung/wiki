---
related_raw: ["[[2026-06-25-jikji_Instant_Search_Indices_for_AI_Agents.md]]"]
tags: ["#wiki", "jikji", "Local-File-Maps", "Agentic-Tools", "Search-Indexing", "Development-Environment"]
---

# jikji: 에이전트 전용 비파괴 로컬 파일 검색 인덱서

**jikji**는 로컬 작업 디렉토리 내에서 행동하는 AI 코딩 에이전트가 시스템 파일 구조를 손상하지 않으면서도, 빠른 문맥 조회를 수행할 수 있도록 돕는 비파괴적 로컬 파일 맵핑 및 실시간 인스턴트 검색 인덱싱 오픈소스 솔루션입니다.

## 1. 강점 및 설계 특징
- **비파괴적 가상화 (Non-destructive)**: 실제 디스크 구조나 Git 메타데이터를 훼손하지 않으면서 로컬 디렉토리의 전체 맵을 고기능 파일 노드 데이터로 안전하게 추출합니다.
- **인스턴트 코드 심볼 조회**: 에이전트가 파일 내부의 함수, 클래스 위치 및 코드 조각을 즉각 질의(query)하고 매칭 결과를 얻어낼 수 있는 초경량 검색 인덱스를 구성하여, 프롬프트 내에 최적의 코드 컨텍스트를 주입하는 지연 시간을 비약적으로 낮춥니다.
- **에이전트 샌드박스 지원**: 격리 샌드박스 내부 VFS(가상 파일 시스템)와 결합되어 외부 파일 액세스에 대한 에이전트 오동작 리스크를 최소화합니다.

## 🔗 연결된 문서
- [[wiki/Agents/Implementation/AgentFS-Architecture-and-SQLite-Filesystem.md]] — SQLite 기반 가상 파일 시스템 및 격리 기술.
- [[wiki/Engineering/Development-Environment/000_Development-Environment-MOC.md]]
