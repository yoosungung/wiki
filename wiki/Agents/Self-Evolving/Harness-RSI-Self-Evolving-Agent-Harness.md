---
id: wiki-harness-rsi-self-evolving-agent-harness
title: "Harness RSI: 가중치 고정 하네스 자가진화의 정의·분류·PAC 승인"
status: canonical
owner: km
updated: "2026-11-09"
last_updated: "2026-11-09"
review_after: "2026-12-09"
tags: ["Agents", "Self-Evolving", "Harness-RSI", "PAC", "Admission"]
sources:
  - https://arxiv.org/abs/2610.18813
  - https://github.com/zgcagi/Harness-RSI
type: wiki
---

# Harness RSI: 가중치 고정 하네스 자가진화의 정의·분류·PAC 승인

[[wiki/Agents/Self-Evolving/Meta2-Precomputed-Harness-Evolution.md|Meta²]]·[[wiki/Agents/Self-Evolving/Harness-S-Sibling-Rescue-Training.md|Harness-S]]·[[wiki/Agents/Self-Evolving/Continual-Harness-Evolution-Catastrophic-Forgetting.md|continual forgetting]]이 **방법 사례**라면, Wei et al. (arXiv:2610.18813) *Self-Evolving Agent Harness*는 **하네스 자가진화(Harness RSI)**를 정의·분류하고 일반화/망각/승인 조건을 정리한 66페이지 프레임워크다. 코드·부록: `https://github.com/zgcagi/Harness-RSI`.

## 1. 정의 (지속 피드백 루프)

하네스 `H`는 고정 모델 `M`의 실행을 지배하는 소프트웨어·설정(루프, 도구/스킬, 컨텍스트, 메모리, compaction, 스케줄, 인프라). 롤아웃 `τ ~ Run(M,H,E)`를 평가기 `J`가 채점한다. 자가진화는 라운드 `k`에서 배치 피드백으로 `H_k = Update(H_{k-1}, B_k)`를 만들고, **승인된 개정만 다음 런에 로드**한다. 필수 조건: (1) 자체 실행 피드백으로 개정을 알고리즘적으로 제안·선택, (2) 승인분이 런 간에 지속. 로그 append·고정 규칙 compaction만으로는 하네스 개정이 아니다.

## 2. 업데이트 대상 분류

| 축 | 내용 | 예 |
| :--- | :--- | :--- |
| Interpreted state | 지시문·저장 경험·고정 연산자 위 라우팅 | 프롬프트/메모리 큐레이션, 워크플로 시퀀스 |
| Tools/code patches | 호출 가능 절차·모듈 구현만 교체 | skill 라이브러리, Self-Harness류 패치 |
| Repository/runtime logic | 오케스트레이션·훅·복구·종료 | whole-agent synthesis, HarnessOpt(런타임 개정) |
| Plugin composition | 선언 인터페이스로 서비스 바인딩·교체 | Everything Is a Plugin(EIP); 생성 도구 마운트 |

분류는 피드백·지속 요건 충족 여부와 독립이다. HarnessOpt+skill은 SpreadsheetBench에서 소형 모델이 대형+SkillOpt를 넘는 **model–harness pairing** 교차 사례를 보고한다(비용 정합 우위 주장 아님).

## 3. 이론 요약 (조건적)

검색은 EA 관점(표현·변이·평가·선택; 엘리트/아카이브/파레토)으로 대응한다. Continual PAC 관점에서 라운드별 외생 분포·독립 샘플 가정 하에 **기대 일반화 경계**, 역사적 회귀 예산에 조건부인 **retention 경계**, 신선·독립 검증 데이터를 쓰는 **고확률 승인 규칙**을 서술한다. 실증 이득만으로 일반화·유지를 단정하지 않는다 — [[wiki/Agents/Self-Evolving/Continual-Harness-Evolution-Catastrophic-Forgetting.md]]의 SWE 94%→32% 관측과 같은 축.

## 4. 시스템 함의

지속 개정이 조직 워크플로·지식 공유·책임에 미치는 영향을 다루. 배포 요건: 태스크 분포·평가기 변화 시 **지속 검증**, 학습·런타임 권한·결과적 행동에 대한 **독립 세이프가드**. Meta²(런 로컬 폐기 편집)와 달리 이 프레임의 기본형은 **승인분이 다음 런에 남는** 지속 개정이다.

## 🔗 관련 문서

- [[wiki/Agents/Self-Evolving/Meta2-Precomputed-Harness-Evolution.md]]
- [[wiki/Agents/Self-Evolving/Harness-S-Sibling-Rescue-Training.md]]
- [[wiki/Agents/Self-Evolving/Harness-Squared-Recursive-Agent-Harnessing.md]]
- [[wiki/Agents/Self-Evolving/Continual-Harness-Evolution-Catastrophic-Forgetting.md]]
- [[wiki/Agents/Self-Evolving/SkillOpt-및-과학적-탐구-멀티-에이전트-시스템.md]]
