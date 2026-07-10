# 뉴스 기반 정치인 신뢰도 및 역량 평가 시스템

## 1. 연구 개요
- **연구 목적**: 뉴스를 통해 정치인의 신뢰, 능력, 도덕성을 평가하는 시스템 연구
- **우선순위**: Low

## 2. 주요 연구 내용 및 지표(Metrics)
### A. 평가 지표 설계 (ABI 프레임워크)
- **능력 (Ability)**: 정책 전문성, 행정 경험, 위기 관리 능력, 공약 이행률.
- **도덕성 (Integrity)**: 법적/윤리적 결함 여부, 언행일치, 정치적 일관성.
- **선의 (Benevolence)**: 소외 계층 관심도, 소통 능력, 공익 우선순위(Self-interest vs Public-interest).

### B. LLM 기반 분석 방법론
- **개체 중심 감성 분석 (Entity-Centric Sentiment Analysis)**: 뉴스 기사 내 특정 정치인에 대한 미디어의 긍정/부정 어조 및 프레임 추출.
- **잠재적 위치 추정 (Latent Position Estimation)**: 발언 및 투표 기록 분석을 통한 이념적 위치 및 정책적 스탠스 수치화.
- **쌍체 비교 (Pairwise Comparison)**: 지표별 비교 프롬프팅과 Bradley-Terry 모델을 결합한 신뢰도 랭킹 산출.

## 3. 주요 도전 과제
- **모델 편향성 관리**: LLM의 내재적 정치 성향이 평가에 미치는 영향 최소화 (불일치 지표 측정).
- **데이터 신뢰성**: 가짜 뉴스 및 편향된 미디어 소스 필터링 기술.
- **환각(Hallucination) 방지**: 실제 사실 관계(Fact)와 정성적 평가의 엄격한 분리.

## 🔍 탐색 매개변수 (Exploration Parameters)
- **Primary Keywords**: `Entity-Centric Political Sentiment Analysis`, `ABI (Ability-Benevolence-Integrity) Politician Trust`, `Political Latent Position Estimation LLM`
- **Secondary Keywords**: `News-based Political Performance Metrics`, `LLM Political Bias Detection Framework`, `Real-time Politician Evaluation NLP`
- **Channels**: `ACL Anthology`, `arXiv (cs.CL, cs.CY)`, `NewsGuard`, `Oxford Academic (Political Science)`
- **Focus**: 뉴스 텍스트에서 정치인의 정성적 지표(신뢰, 도덕성 등)를 정량화하는 LLM 방법론 및 모델의 정치적 편향성 관리 기술 조사.

## 3. 진행 상태
- 아이디어 구체화 단계 (2026-04-22)

