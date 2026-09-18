---
title: GraphRAG-vs-LightRAG-2026
related_raw:
  - "[[raw/2026-09-15-lightrag-v1.5.7-workspace-pgtable.md]]"
  - "[[raw/2026-09-16-graphiti-v0.30.2-neo4j-falkordb.md]]"
  - "[[raw/2026-09-19-graphiti-local-readonly-mcp.md]]"
tags:
  - wiki
  - ai_core
  - ai
type: wiki
status: draft
last_updated: "2026-09-19"
updated: "2026-09-19"
---

# 📊 GraphRAG vs LightRAG: 2026년 성능 및 아키텍처 비교

2026년 현재 지식 그래프 기반 RAG(GraphRAG) 기술은 단순한 벡터 검색을 넘어 정적 전역 요약, 동적 온디맨드 인덱싱, 그리고 에이전트 전용 시공간(Bi-temporal) 메모리로 분화 발전하고 있습니다.

## 1. 2026년 주요 그래프 RAG 아키텍처 비교

| 기능 | GraphRAG (Microsoft) | LightRAG (HKU) | LazyGraphRAG (MSR) | Graphiti (Zep) |
| :--- | :--- | :--- | :--- | :--- |
| **주요 목적** | 정적 말뭉치 전역 요약 | 복합 문서 다단계 검색 | 질의 시점 온디맨드 검색 | **에이전트 장기 메모리** |
| **질의 비용** | 높음 (수백 개 API 호출/질의) | **초저비용** (단일 API 호출) | 저비용 (부분 하위그래프) | 초저비용 (<200ms P95) |
| **인덱싱 방식** | 비쌈 (전체 재구축 필요) | **증분(Incremental)** 추가 | **사전 요약 생략(Lazy)** | **실시간 이벤트/에피소드** |
| **시간 축 지원** | 미지원 (정적 스냅샷) | 기본 지원 | 미지원 | **Bi-temporal (유효 구간)** |
| **핵심 기술** | Leiden 커뮤니티 감지 | Dual-Level (저수준+고수준) | On-demand Subgraph 탐색 | Temporal Edge & Neo4j |
| **서빙 인터페이스** | Python SDK / CLI | FastAPI REST & WebUI | Python SDK | **MCP Server & Python async** |

## 2. 기술적 차별점

### 1) 검색 전략 (Retrieval Strategy)
- **GraphRAG:** 계층적 요약과 커뮤니티 감지를 사용하여 "이 데이터셋의 주요 테마는 무엇인가?"와 같은 전역적인 질문에 답변하는 데 강점을 보입니다.
- **LightRAG:** **이중 레벨 검색(Dual-Level Retrieval)** 시스템을 사용합니다. 특정 엔티티/관계를 추출하는 저수준 키와 광범위한 테마 컨텍스트를 제공하는 고수준 키를 병렬로 실행하여 효율성을 극대화합니다.
- **Graphiti:** 시간 흐름에 따른 지식의 변화를 추적합니다. 사용자의 선호도나 상태 변화가 발생하면 이전 사실을 덮어쓰지 않고 "유효 기간(validity window)"을 갱신하여, 에이전트가 "과거의 상태"와 "현재의 사실"을 구분하여 추론하도록 지원합니다.

### 2) 운영 지속 가능성 및 인덱싱 비용
- GraphRAG는 초기 대규모 전수 인덱싱 비용이 매우 높아 프로덕션 도입의 진입장벽이 존재합니다.
- **LightRAG**는 신규 문서 유입 시 그래프의 기존 노드와 엣지만을 점진적으로 업데이트(Incremental Indexing)하므로, 일 단위로 지식이 누적되는 위키나 기업 문서 환경에 최적화되어 있습니다.
- **LazyGraphRAG**는 사전 전역 요약(Upfront summarization) 단계를 제거하고 질의 발생 시점에 필요한 하위 그래프만 지연 생성하여 인덱싱 비용을 80% 이상 절감합니다.

## 3. 2026년 차세대 그래프 접근법
- **Graphiti (Zep)**: 에이전트 메모리 전용 오픈소스 프레임워크로, bi-temporal 모델과 Neo4j/메모리 그래프를 통해 에이전트의 대화 세션 간 사실 진화를 sub-200ms 속도로 인출합니다.
- **HippoRAG 2:** 해마(Hippocampus) 신경 생리학적 인덱싱을 모방하여 다중 홉 연상과 단순 팩트 검색의 속도를 획기적으로 개선했습니다.
- **T²RAG (Graph-Free Triplet Retrieval):** 공식적인 그래프 데이터베이스 구축 없이 질의를 트리플릿(Triplet)으로 분해하여 그래프 연산 오버헤드를 제로화한 경량 접근법입니다.

## 4. 아키텍처 선택 가이드
- **LightRAG 선택:** 대규모 규정집, 매뉴얼, 위키 지식 베이스를 상대로 빠른 응답 속도와 지속적인 문서 추가·업데이트가 필요한 엔터프라이즈 RAG 시스템.
- **Graphiti 선택:** 멀티턴 대화, 사용자 프로필 진화, 장기 목표 추적 등 시간에 따라 사실이 변경되는 자율 에이전트(Autonomous Agent)의 롱텀 메모리 레이어.
- **LazyGraphRAG 선택:** 초기 인덱싱 예산이 제한적이며 사전 전역 분석보다는 개별 질의의 심층 추론이 우선인 대규모 비정형 데이터셋.

## 5. API 및 에이전트 연동 패턴
- **LightRAG**: FastAPI 기반 REST 엔드포인트를 내장하여 Docker 컨테이너 및 WebUI로 손쉽게 기동 가능.
- **Graphiti**: `graphiti-core` 파이썬 패키지와 Model Context Protocol(MCP) 서버를 공식 지원하여 Cursor, Claude Desktop, Goose 등 에이전트 클라이언트에 즉시 도구로 마운트 가능. **0.30.x**부터 Neo4j `execute_query`·MCP `NEO4J_DATABASE` 정렬과 FalkorDB fulltext 스캔 제거가 들어갔으므로 셀프호스트 업그레이드 시 [[wiki/RAG/Graphiti-Driver-Abstraction.md]]·[[wiki/RAG/Graphiti-MCP.md]]를 함께 본다. 로컬에서 쓰기 없이 사람 승인 큐만 필요하면 `graphiti-local` 0.4.1(core `0.30.1` 핀, LadybugDB) — 같은 MCP 노트.

## 6. LightRAG v1.5.7 운영 패턴 (2026-09-02)

프로덕션에 넘길 때 **관리자 WebUI**와 **엔드유저 질의 표면**을 분리한다.

| 축 | 패턴 | 구현 힌트 |
| :--- | :--- | :--- |
| **듀얼 엔트리** | 운영자 UI vs 질의 전용 UI | 엔드유저는 `/workspace` — 문서/KG/API-docs 링크 없음(모바일 채팅만) |
| **브랜딩 번들** | 재빌드 없이 로고·환영·동의문 | `UI_TEMPLATES_DIR` + `manifest.json` Markdown 번들(`docs/ui_templates_example/`) |
| **전역 역할 프롬프트** | 배포 단위 톤/포맷 고정 | `USER_PROMPT_PREFIX` / `USER_PROMPT_PREFIX_FILE` — 클라이언트가 읽거나 덮어쓸 수 없음; API만 `disable_user_prompt_prefix`로 옵트아웃 |
| **graph-first ingest** | 벡터 인덱싱 지연 | 그래프를 먼저 쌓고 벡터는 deferred — 대량 유입 시 인덱싱 피크 완화 |
| **청킹 선택** | 파이프라인 명시 | custom chunking selector로 Fix/Recursive 등 전략을 문서군별로 고정 |
| **Postgres all-in-one** | AGE 의존 축소 | `PGTableGraphStorage`(네이티브 테이블)가 AGE 기반 `PGGraphStorage` 대비 선호; AGE→PG 오프라인 마이그레이션 도구 제공. **AGE ≥ 1.8.0**에서는 `PGGraphStorage`를 거부(크래시 가드) |

```bash
# 개념: 엔드유저 전용 표면 + 템플릿 번들
export UI_TEMPLATES_DIR=./docs/ui_templates_example
export USER_PROMPT_PREFIX="답변은 한국어. 인용은 [n] 형식. Mermaid만 사용."
# /workspace → 채팅만; 관리자 엔트리는 문서·그래프 유지
```

참고: [LightRAG v1.5.7 release](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.7), [[wiki/RAG/LightRAG-Summary-2026.md]]

---
## 🔗 관련 링크 및 참고 자료
- LightRAG 공식 리포지토리: [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)
- Graphiti 공식 리포지토리: [getzep/graphiti](https://github.com/getzep/graphiti)
- 관련 위키: [[wiki/RAG/000_RAG-MOC.md]], [[wiki/RAG/Contextual-Retrieval-Anthropic-2026.md]], [[wiki/Agents/Implementation/Supermemory-Architecture-and-MCP.md]], [[wiki/RAG/LightRAG-Summary-2026.md]]
