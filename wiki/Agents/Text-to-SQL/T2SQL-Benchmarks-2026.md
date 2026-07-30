---
title: "T2SQL 벤치마크 2026: 엔터프라이즈 데이터 분석 성능 평가 표준"
tags: ["T2SQL", "Benchmark", "Spider-2.0", "BIRD", "Evaluations"]
type: "wiki"
status: "published"
last_updated: "2026-07-30"
updated: "2026-07-30"
related_raw: ["[[raw/2026-04-28-Spider-2-0-SOTA-Updates.md]]", "[[raw/2026-04-29-Spider2-OSI-Updates.md]]", "[[raw/2026-05-08-daily-research-data.md]]"]
---

# T2SQL 벤치마크 (2026)

2026년 Text-to-SQL(T2SQL) 분야는 단순한 쿼리 생성을 넘어, 엔터프라이즈 환경의 복잡한 워크플로우를 평가하는 방향으로 진화했습니다. 다음은 현재 업계 표준으로 자리 잡은 핵심 벤치마크들입니다.

## 🏆 핵심 벤치마크 분석

### 1. Spider 2.0: 엔터프라이즈 SQL 워크플로우 평가
Spider 2.0은 실제 기업 환경의 대규모 데이터베이스 구조와 실무적인 SQL 쿼리 생성 능력을 평가하기 위해 설계되었습니다.
- **특징**: 수천 개의 컬럼(1,000+)을 가진 복잡한 클라우드 데이터 웨어하우스(BigQuery, Snowflake) 환경을 반영합니다.
- **난이도**: Spider 1.0에서 90% 이상을 기록하던 모델들이 초기에는 **5~25% 수준**으로 정확도가 급락하는 '성능 절벽'을 보였으나, 2026년 현재 에이전틱 워크플로우를 통해 80%선까지 극복하고 있습니다.
- **2026년 4월 최신 순위**:
    - **Spider 2.0 Snow Track 1위**: **[[wiki/Agents/Text-to-SQL/Genloop-Sentinel|Genloop's Sentinel Agent v2 Pro]]** (96.70%). 'Unified Business Memory'와 컨텍스트 그래프 추론을 통해 비즈니스 로직(예: 매출 정의)을 정확히 파악하여 독보적인 1위 유지.
    - **Spider 2.0 Snow Track 2위**: **Native mini** (96.53%).
    - **Spider 2.0 Lite 1위**: **[[wiki/Agents/Text-to-SQL/Oracle-SOMA-SQL|Oracle SOMA-SQL]]** (72.02%). 'Reasoning-driven' 프레임워크를 통해 기업 데이터의 모호성을 해결하며 Lite 트랙 최고 기록 경신 (2026.04.23).
    - **Spider 2.0 Lite 2위**: **Databao Agent (JetBrains)** (69.65%).
    - **Spider 2.0 Lite 3위**: **AV-SQL** (70.38% - 이전 기록 기준 2위였으나 현재 Oracle에 의해 갱신됨). 'Agentic Views' 기법을 도입하여 대규모 스키마를 CTE 형태로 분해 처리.

### 2. BIRD (Big Bench for Large-scale Database Grounded Text-to-SQL Evaluation)
BIRD는 대규모 데이터베이스 기반의 실행 정확도(Execution Accuracy)를 중점적으로 평가합니다.
- **성과**: 2026년 3월, **ReViSQL** 프레임워크가 인간의 실행 정확도인 **93.78%**를 돌파하며 역사적인 지표를 달성했습니다.
- **주요 기법**: RLVR(Reinforcement Learning via Verification)을 통해 실제 결과값(Value)의 일치 여부를 학습에 반영합니다.

### 3. BIRD-Interact & BIRD-Critic
- **BIRD-Interact**: 대화형 데이터 분석 능력을 평가합니다. 모호성 해소(Ambiguity Resolution), 오류 복구, 사용자 피드백 반영 능력을 측정합니다.
- **BIRD-Critic-SQLite**: 생성된 SQL의 오류를 스스로 찾아내고 수정하는 **디버깅(Debugging)** 능력을 평가합니다.

## 🚀 주요 기술 트렌드 및 성능 모델

### 1. Qwen2.5-Coder 시리즈
Alibaba의 Qwen2.5-Coder는 오픈소스 모델임에도 불구하고 T2SQL 분야에서 독보적인 성능을 보여줍니다.
- **Qwen2.5-Coder-32B-Instruct**: 특정 파이프라인에서 **95.73%**의 정확도를 기록하며 GPT-4.5 Turbo와 같은 상용 모델을 능가했습니다.

### 2. CogniSQL-R1-Zero (7B)
GRPO(Group Relative Policy Optimization)를 통해 순수 실행 보상만으로 학습된 sLM 모델입니다.
- **성과**: 7B 규모로 수천억 파라미터급 모델의 성능을 재현하며 효율적 추론의 가능성을 입증했습니다.

### 3. Talon Models (7B/14B)
BIRD-Critic 환경에서 최적의 성능을 내도록 설계되었으며, 복잡한 조인 구조와 윈도우 함수 오류를 수정하는 능력이 극대화된 모델입니다.

## 📊 평가 지표의 변화
- **Execution Correctness (EX)**: 쿼리의 문법적 정확도보다 실제 실행 결과값의 일치 여부를 핵심 지표로 삼습니다.
- **R-VES (Relative Value Estimation Score)**: 쿼리의 실행 효율성(Execution efficiency)까지 고려하여 점수를 산출합니다.

## 🧪 nl2sql 제품 품질 게이트 (Spider2-Lite local*, 2026-07-29 → verified 2026-07-30)

제품 레포 `spider2-eval`의 채점 정본도 동일하게 **EX/exec_result**(예측 SQL 실행 결과 ↔ gold CSV)이며 SQL 문자열 일치가 아니다.

- 스모크 instance: `local008`(Baseball), `local022`(IPL) — `QUALITY_SMOKE_INSTANCE_IDS`
- Preflight: `spider2-load-pg` → `spider2-opik-upload-exec` → `spider2-opik check` → `gold-sql` + `--instance-ids`
- **2026-07-30 실측**: in-cluster FQDN + Opik project `nl2sql` 재생성 후 `gold-sql` smoke pass_rate **1.0**. PR#17 머지는 `backend`+`mcp` Test green 필요.
- `--task agent`는 AC만 고정(구현 후속). UI Playwright와 축 분리.
- 상세 canonical: [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]

## 💡 AX1센터 R&D 시사점
- **평가 체계 전환**: 단순 Accuracy를 넘어 **Execution Correctness** 중심의 평가 체계(BIRD-Verified 기반)로의 완전 전환이 필요합니다.
- **데이터 정제 루프**: 인간 피드백 대신 실행 결과 기반의 자율 검증(RLVR) 루프 구축이 필수적입니다.
- **에이전틱 접근법**: 단순 모델 성능보다 워크플로우 제어와 컨텍스트 최적화 전략을 사용하는 에이전트 기반 접근법이 순위를 결정짓는 핵심 요소입니다.

## 🔗 관련 문서
- [[wiki/Agents/Text-to-SQL/ThoughtSpot-Spotter-Semantics]]
- [[wiki/Agents/Text-to-SQL/Agentic-Semantic-Layer]]
- [[wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md]]
- [[wiki/Agents/Frameworks/Evaluations/000_Evaluations-MOC]]
