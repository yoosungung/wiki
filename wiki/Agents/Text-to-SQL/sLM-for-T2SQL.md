---
title: "T2SQL을 위한 소형 언어 모델(sLM) 전략"
related_raw: ["[[raw/2026-04-18-AI-Coder-and-sLM-T2SQL-Research]]"]
tags: ["wiki", "T2SQL", "sLM", "LLM", "Optimization"]
type: "wiki"
status: "complete"
last_updated: "2026-04-19"
---

# Text-to-SQL 고도화를 위한 sLM 활용

T2SQL 분야에서 sLM(Small Language Models)은 낮은 지연 시간(Latency)과 저렴한 비용으로 상용 모델급의 효율을 내기 위한 핵심 요소입니다.

## 💎 추천 sLM 모델 (2026년 기준)

| 모델명 | 크기 | 강점 |
| :--- | :--- | :--- |
| **Qwen 2.5 Coder 7B** | 7B | **로컬 표준.** GPT-4o급 SQL 생성력과 탁월한 한국어 처리 능력. |
| **BIRD-Talon-7B** | 7B | **T2SQL 특화.** 실제 기업용 DB의 복잡하고 지저분한 스키마 해석에 최적화. |
| **DeepSeek-V2-Lite** | 2.4B(A) | **MoE 효율.** 적은 연산량으로 방대한 스키마를 처리하는 높은 컨텍스트 효율성. |
| **Phi-4-mini** | 3.8B | **논리 추론.** 복잡한 Join 및 서브쿼리 문법 생성 시 높은 정밀도. |

## 🛠️ 성능 극대화 전략

### 1. Schema-RAG (Context Pruning)
- 수천 개의 컬럼 중 질문과 관련된 테이블/컬럼만 동적으로 선별하여 sLM의 입력 제한(Context Window) 문제를 해결하고 할루시네이션을 방지합니다.

### 2. 세만틱 레이어(Semantic Layer) 연동
- sLM이 복잡한 Raw SQL을 직접 생성하는 대신, **dbt Semantic Layer**나 **Cube**의 메트릭을 호출하도록 설계하여 정확도를 90% 이상 확보합니다.

### 3. 에이전틱 자기 교정 (Agentic Self-Correction)
- sLM이 SQL을 생성한 후 직접 실행해 보고, 발생한 에러 메시지를 바탕으로 쿼리를 스스로 수정하는 루프를 구축합니다. 이는 sLM의 부족한 '한 번에 완벽한 생성 능력'을 보완합니다.

## 📊 주요 벤치마크 지표
- **Spider 2.0**: 실무급 복잡한 워크플로우 대응력 평가.
- **BIRD**: 비즈니스 용어와 DB 스키마 간의 매핑 정확도 측정.

## 🔗 관련 문서
- [[wiki/Agents/Text-to-SQL/DeepAgent-T2SQL]]
- [[T2SQL_Planning]]
- [[wiki/Agents/Text-to-SQL/Spider-2.0]]
- [[wiki/Engineering/AI-Native-Engineering/Coder-Models-2026]]
