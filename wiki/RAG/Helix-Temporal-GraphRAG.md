---
id: helix-temporal-graphrag
title: "Helix Temporal GraphRAG (LightRAG + Graphiti 결합)"
status: canonical
owner: km
updated: "2026-09-22"
last_updated: "2026-09-22"
review_after: "2026-12-21"
related_raw:
  - "[[raw/2026-09-22-helix-temporal-graphrag-lightrag-graphiti.md]]"
sources:
  - https://github.com/YashNuhash/Helix
  - https://pypi.org/project/helix-rag/0.2.0/
  - https://github.com/HKUDS/LightRAG
  - https://github.com/getzep/graphiti
tags: ["RAG", "GraphRAG", "LightRAG", "Graphiti", "Temporal"]
type: "wiki"
---

# Helix Temporal GraphRAG (LightRAG + Graphiti 결합)

연구·프로토타입 패키지 **Helix**(`helix-rag` PyPI **0.2.0**, MIT, Alpha)는 LightRAG의 이중 레벨 검색과 Graphiti의 bi-temporal KG를 한 런타임으로 묶는다. Figure AI의 Helix VLA와 **동명이며 별개**다 — [[wiki/Agents/Robotics-and-VLA/Figure-03-Helix-VLA-Stack.md]].

## 역할 분담

| 계층 | 역할 |
|------|------|
| LightRAG | 청킹·임베딩·dual-level 검색·증분 인덱싱 |
| Graphiti | 에피소드 인제스트, bi-temporal 유효 구간, 엣지 invalidate |
| Helix 모듈 | TemporalHandler, MultiHopRetriever(BFS), HallucinationDetector(CFI) |

스토리지: **Neo4j 필수**(Graphiti), Supabase는 벡터 옵셔널.

## 설치·환경

```bash
pip install helix-rag
# 또는
git clone https://github.com/YashNuhash/Helix.git && cd Helix && pip install -e ".[helix]"
```

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=...
LLM_MODEL_NAME=...
LLM_API_KEY=...
# optional: SUPABASE_URL / SUPABASE_KEY
```

의존성 메타데이터는 `graphiti-core>=0.27.1`이다. org-wiki 정본 스택은 Graphiti **0.30.2**·LightRAG **v1.5.7**이므로, Helix를 올릴 때 **코어 핀을 재검증**한다 — [[wiki/RAG/Graphiti-Overview.md]], [[wiki/RAG/LightRAG-Summary-2026.md]].

## 구현 패턴

```python
import asyncio
from datetime import datetime
from helix import Helix

async def main():
    async with Helix() as helix:
        await helix.insert(
            "Alan Turing was born on June 23, 1912.",
            source_description="Wikipedia",
        )
        # hybrid = LightRAG dual-level
        ans = await helix.query("When was Alan Turing born?", mode="hybrid")
        # point-in-time
        past = await helix.query(
            "What was the CEO of Apple in 2015?",
            valid_at=datetime(2015, 1, 1),
            include_temporal_context=True,
        )
        print(ans, past)

asyncio.run(main())
```

환각 게이트: `HallucinationDetector(graphiti=...).verify_response(...)` → `is_grounded`, CFI `confidence_score`, `entity_coverage`. 다중 홉: `MultiHopRetriever.find_paths(query=..., max_hops=3)` 후 `format_paths_as_context`.

## 벤치마크 목표 vs 현실

README의 Hit@1 70–75%·CFI>0.95·토큰 <600K 등은 **연구 목표치**다. Alpha 상태이므로 KM/에이전트 메모리에 넣기 전 (1) Graphiti 0.30.x 호환, (2) Neo4j DB 라우팅(`NEO4J_DATABASE`), (3) LightRAG `/workspace`·PGTable 경로와의 중복 책임을 점검한다.

## 선택 가이드

- **Helix를 쓸 때**: LightRAG 문서 RAG + Graphiti 시간축을 **한 패키지 API**로 빠르게 프로토타입할 때.
- **직접 조합할 때**: 이미 LightRAG 서버와 Graphiti MCP를 분리 운영 중이면 Helix 없이 [[wiki/RAG/GraphRAG-vs-LightRAG-2026.md]] 선택 가이드대로 연동하는 편이 핀·업그레이드가 단순하다.

## 🔗 관련 문서

- [[wiki/RAG/GraphRAG-vs-LightRAG-2026.md]]
- [[wiki/RAG/Graphiti-Architecture.md]]
- [[wiki/RAG/Graphiti-MCP.md]]
- [[wiki/RAG/LightRAG-Summary-2026.md]]
