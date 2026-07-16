---
title: "T2SQL 트렌드 업데이트 (2026-04-26)"
tags: ["T2SQL", "Spider-2.0", "GRPO", "Genloop", "Oracle"]
type: "wiki"
status: "published"
last_updated: "2026-07-14"
updated: "2026-07-14"
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

## 3. 시맨틱 레이어 표준화 (Apache Ossie)
- Open Semantic Interchange(OSI)는 **Apache Ossie**로 이전됨. 최신 안정 명세는 0.1.1이고 0.2.0.dev0은 미출시 초안이며, `ai_context`로 에이전트용 지침·동의어·예시를 표현함.
- Snowflake와 ThoughtSpot의 네이티브 통합 사례는 에이전트 분석 도구의 상호운용성(Interoperability) 확보를 가속화할 전망.

## 4. 향후 대응 전략 (AX1센터)
- **GRPO 학습 도입**: 내부 데이터셋을 활용하여 실행 보상 기반의 RL 파이프라인 구축 실험 필요.
- **Ossie 명세 검증**: 안정판 스키마를 고정하고 변환 전후 호환성을 회귀 테스트하며, 개발판은 별도 시험 환경에서 평가.
- **AV-SQL 기법 벤치마킹**: 대규모 스키마 처리를 위한 '에이전틱 뷰(Agentic Views)' 기법을 내부 아키텍처에 이식.

## 관련 문서
* [[wiki/Agents/Text-to-SQL/T2SQL-Benchmarks-2026]]
* [[wiki/Agents/Text-to-SQL/GRPO-for-T2SQL]]
* [[wiki/Engineering/Data-and-Security/OSI-Open-Semantic-Interchange]]
