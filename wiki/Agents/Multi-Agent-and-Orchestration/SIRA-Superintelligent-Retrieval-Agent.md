---
title: "SIRA: Superintelligent Retrieval Agent (초지능형 검색 에이전트)"
tags: ["Agents", "MAS", "RAG", "SIRA", "Retrieval", "Context-Engineering"]
type: "wiki"
status: "published"
last_updated: "2026-07-01"
updated: "2026-07-01"
related_raw: []
---

# 🔍 SIRA: Superintelligent Retrieval Agent (초지능형 검색 에이전트)

## 1. 개요 및 등장 배경
**SIRA (Superintelligent Retrieval Agent)**는 2026년 5월 Meta의 Superintelligence Lab에서 발표한 혁신적인 RAG(Retrieval-Augmented Generation) 검색 프레임워크입니다. 

기존의 에이전틱 RAG(Agentic RAG) 환경에서는 복잡한 질의를 해결하기 위해 에이전트가 탐색적 쿼리를 던지고, 검색 결과에 따라 쿼리를 재포뮬레이션하는 **다단계 반복 검색(Iterative Multi-step Search)** 방식을 주로 채택했습니다. 하지만 이 방식은 다음과 같은 치명적인 한계를 가집니다.
* **추론 레이턴시(Latency) 급증**: 매 회차 검색 시마다 LLM의 Generation 루프와 검색 인덱스 호출이 순차 실행되어 실시간 서비스가 불가능해집니다.
* **컨텍스트 오염 및 비용 오버헤드**: 여러 라운드를 거치며 대화 컨텍스트 창이 쓸데없는 검색 파편으로 오염되고 API 비용이 누적됩니다.
* **초기 타겟팅 실패**: 첫 번째 루프에서 방향을 잘못 설정하면 이후의 모든 다단계 검색이 빗나가는 "Cascade Error"가 발생합니다.

SIRA는 LLM의 인지 능력을 검색 인덱스에 결합하여, 이러한 탐색 과정을 **단 한 번의 고도로 판별적인 검색 액션(Single-shot discriminative retrieval action)**으로 압축하여 RAG의 구조적 패러독스를 해결합니다.

---

## 2. 핵심 아키텍처 및 작동 프로세스
SIRA는 검색 시스템이 데이터베이스의 지식 분포를 완벽히 꿰뚫고 있는 **"도메인 전문가(Expert)"**처럼 기능하도록 설계되었습니다. 작동 원리는 크게 두 단계로 분리됩니다.

```mermaid
flowchart TD
    subgraph Offline ["오프라인 단계 (Corpus Enrichment)"]
        D[원본 문서 수집] --> LLM1[Frozen LLM 어휘 분석]
        LLM1 -->|동의어 / 전문 용어 / 약어 추출| I[누락 어휘 주입]
        I --> DF[DF 문서 빈도 통계 필터링]
        DF -->|식별력 검증 완료| Index[색인 데이터베이스 반영]
    end
    
    subgraph Online ["온라인 단계 (Query-Side Enrichment)"]
        Q[사용자 복잡 쿼리 입력] --> LLM2[Expected-Response Sketch 작성]
        LLM2 -->|예상 답변 텍스트 구조 설계| K[가중 키워드 추출]
        K --> V[어휘 사전 검증 및 필터링]
        V -->|원래 쿼리와 결합| BM25[Weighted BM25 단일 검색 호출]
        BM25 --> R[고정밀 최종 컨텍스트 추출]
    end
```

### 1) 오프라인: 코퍼스 풍부화 (Offline Corpus Enrichment)
* **목적**: 검색 쿼리에 쓰일 가능성이 높지만 원본 문서에는 명시적으로 표기되지 않은 지식 공백을 메웁니다.
* **어휘 사전 주입**: 고정된 LLM(frozen LLM)이 코퍼스 내부의 문서를 한 번씩 읽으면서, 해당 도메인의 핵심 키워드, 동의어, 축약어, 대체 용어 등을 주입합니다.
* **문서 빈도(DF) 통계 필터링**: 주입된 단어가 지나치게 일반적일 경우(예: '데이터', '시스템') 검색 분별력을 저해하므로, 문서 빈도(Document-frequency) 통계를 비교하여 식별력이 높은 엣지 어휘만 필터링하여 색인에 통합합니다.

### 2) 온라인: 쿼리측 풍부화 (Online Query-Side Enrichment)
* **목적**: 사용자의 모호하고 복잡한 의도를 최종 정답 데이터의 텍스트 레이아웃과 일치시킵니다.
* **예상 답변 스케치 (Expected-Response Sketch)**: 사용자의 질의가 입력되면, LLM은 검색 전 정답에 들어갈 법한 "증거 문장의 예상 구조와 단어군"을 먼저 예측하여 설계(Sketching)합니다.
* **단일 가중치 검색**: 예측된 어휘 사전을 인덱스 내부 용어들과 일차 검증한 후, 원래 사용자의 질문과 가중 결합하여 단 한 번의 가중치 기반 **BM25(또는 learned sparse retrieval) API**를 호출합니다.

---

## 3. 기술적 이점 및 벤치마크 결과
* **RAG 패러독스 해결**: 여러 단계를 수행하는 Multi-hop Agentic RAG의 검색 정밀도(Recall)를 능가하면서도, 검색 지연 시간은 일반 키워드 검색 엔진의 1회 호출 수준(300ms 미만)으로 억제합니다.
* **훈련 불필요(Training-free)**: Vector DB를 세팅하거나 별도의 임베딩 파인튜닝 프로세스를 거치지 않고, 기존 Lexical/Hybrid 검색 시스템에 프롬프트 코그니션(Cognition)을 결합하여 고성능을 냅니다.
* **BrowseComp-Wikipedia 실증**: 2,500만 개 이상의 거대 문서 스케일에서 정합성을 확인하기 위해 설계된 난해한 탐색형 쿼리 평가(232개 복합 질의군)에서 기존 Dense Retriever(Cohere, BGE 등)와 Multi-round Agentic baseline 대비 월등한 NDCG@10 성능 향상을 증명했습니다.

---

## 4. 멀티 에이전트 시스템(MAS)과의 통합 시나리오
SIRA는 MAS 환경에서 다른 협업 에이전트에게 필요한 컨텍스트를 주입하는 **최우선 관문 에이전트(Gateway Agent)**로 작동합니다.
* **OpenClaw 와의 연동**: OpenClaw의 5대 서브시스템 중 **Active Memory** 레이어에 탑재되어, 의사 결정 브레인(Brain)이 도구를 실행하기 전 필요한 지식을 단 한 번의 스텝으로 고속 RAG 검색하여 주입합니다.
* **Supervisor-Worker 구조 최적화**: Supervisor 모델이 지식을 수집하기 위해 Worker 에이전트들을 여러 개 생성하여 탐색을 지시하던 비효율적인 분산 구조를 제거하고, SIRA 단일 에이전트가 단일 액션으로 가공된 지식을 복구하여 Supervisor에게 다이렉트로 전달합니다.

---
**관련 문서**:
- [[wiki/Agents/Multi-Agent-and-Orchestration/OpenClaw-및-HyperAgent-기반-MAS-아키텍처.md]]
- [[wiki/Agents/Multi-Agent-and-Orchestration/000_Multi-Agent-and-Orchestration-MOC.md]]
