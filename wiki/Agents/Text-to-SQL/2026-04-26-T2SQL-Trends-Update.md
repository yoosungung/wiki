---
title: "T2SQL 트렌드 업데이트 (2026-04-26)"
tags: ["T2SQL", "Spider-2.0", "GRPO", "Genloop", "Oracle"]
type: "wiki"
status: "published"
last_updated: "2026-04-26"
---

# T2SQL 트렌드 업데이트 (2026-04-26)

## 1. 리더보드 지각 변동: Spider 2.0 Snow 1위 교체
- **[[wiki/Agents/Text-to-SQL/Genloop-Sentinel|Genloop Sentinel Agent v2 Pro]]**가 **96.70%**라는 경이로운 정확도로 Snowflake 트랙(Snow) 1위를 차지함.
- 기존 강자였던 **ByteBrain-Agent (84.10%)**를 큰 차이로 따돌리며, 에이전틱 워크플로우의 완성도가 성능의 핵심임을 재입증.
- **[[wiki/Agents/Text-to-SQL/Oracle-SOMA-SQL|Oracle SOMA-SQL]] (72.02%)**이 Lite 트랙 1위에 오르며, 상용 DB 벤더들의 직접적인 기술 참전이 가속화됨.

## 2. 기술적 패러다임 시프트: GRPO 기반 RL의 정착
- 단순 SFT(지도 학습)를 넘어, **GRPO (Group Relative Policy Optimization)**를 활용한 실행 보상 기반 강화학습이 표준화됨.
- **CogniSQL-R1-Zero** 사례처럼 7B급 소형 모델이 실행 정확도 보상만으로 GPT-4o급 성능을 내는 '가성비 최적화'가 대세.
- 쿼리 정확도와 더불어 **실행 비용(Cost-Awareness)**을 보상 함수에 통합하려는 시도가 관측됨.

## 3. 시맨틱 레이어 표준화 (OSI v1.0)
- **OSI v1.0** 공식 사양 발표와 함께 `ai_context` 필드가 추가되어, 에이전트가 비즈니스 지표를 더 정확히 이해할 수 있는 인프라가 구축됨.
- Snowflake와 ThoughtSpot의 네이티브 통합 사례는 에이전트 분석 도구의 상호운용성(Interoperability) 확보를 가속화할 전망.

## 4. 향후 대응 전략 (AX1센터)
- **GRPO 학습 도입**: 내부 데이터셋을 활용하여 실행 보상 기반의 RL 파이프라인 구축 실험 필요.
- **OSI 표준 준수**: 개발 중인 시맨틱 모델링 도구를 OSI v1.0 사양에 맞춰 업데이트하여 외부 에이전트와의 호환성 확보.
- **AV-SQL 기법 벤치마킹**: 대규모 스키마 처리를 위한 '에이전틱 뷰(Agentic Views)' 기법을 내부 아키텍처에 이식.

## 관련 문서
* [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026]]
* [[wiki/Agents/Text-to-SQL/GRPO-for-T2SQL]]
* [[wiki/Engineering/Data-and-Security/OSI-Open-Semantic-Interchange]]
