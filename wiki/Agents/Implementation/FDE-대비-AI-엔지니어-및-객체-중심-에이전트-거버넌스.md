---
related_raw: ["[[2026-06-29-fde-vs-ai-engineer-and-object-centric-agents.md]]"]
tags: ["#wiki", "Agents/Implementation", "Agents/Trends", "Object-Centric", "Governance"]
---

# FDE 대 AI 엔지니어 및 객체 중심(Object-Centric) 에이전트 거버넌스

기업들의 AI 도입 및 AX(AI Transformation)가 가속화되면서 에이전트 개발 조직의 구성 형태와 대규모 에이전트 무리를 관리하는 방식의 아키텍처적 진화가 동시에 논의되고 있습니다.

## 1. FDE (Forward Deployed Engineer) 모델의 한계와 AI Engineer의 부상
- **FDE 모델의 현황**: 현재 대다수 국내 AX 컨설팅은 외부 전문가가 고객사의 비즈니스 프로세스를 파악하여 맞춤형 AI 워크플로우를 구축해 주는 FDE 모델 형태를 띠고 있습니다.
- **앤드류 응(Andrew Ng)의 분석**:
  - 장기적으로는 FDE보다 사내에서 지속적으로 AI 시스템을 고도화하고 운영할 수 있는 **사내 AI 엔지니어(Internal AI Engineer)**의 수요가 더욱 급증할 것입니다.
  - FDE의 역할은 대개 특정 벤더 제품에 강결합된 밀착 컨설팅인 경우가 많아, 급변하는 LLM 생태계 내에서 기업의 기술적 유연성(Optionality)과 선택권을 박해받을 위험이 있습니다.
- **AX 전환의 실천 방향**:
  - 외부 전문가의 단발성 데모 구축에서 벗어나, 기업 내부 구성원들이 선언적으로 에이전트를 정의하고, 프롬프트와 도구를 분리 관리하며, Eval(평가 기준) 시스템을 축적할 수 있는 프레임워크 역량을 내재화해야 합니다.

## 2. 객체 중심(Object-Centric) 에이전트 상태 및 실행 아키텍처
에이전트의 개수가 폭발적으로 증가하여 수십, 수백 개가 작동하는 엔터프라이즈 환경에서는 개별 에이전트를 인간이 수작업으로 제어하기 불가능해집니다. 이때 **"누가 에이전트를 조율하는가"**보다 **"어떤 규격으로 정보가 유통되는가"**로 관리 패러다임이 시프트합니다.

- **개념**: 데이터 및 비즈니스 규약 문서 자체를 단순 텍스트 파일이 아닌 **상태(State), 권한(Permission), 책임(Responsibility), 정책(Policy), 실행 이력(History)을 갖춘 '객체(Object)'**로 추상화하는 아키텍처입니다.
- **핵심 장점**:
  - 모델 라우팅이나 특정 개발 벤더가 바뀌더라도, 데이터 객체 내에 내재된 권한과 규약이 규율되므로 거버넌스가 안정적으로 유지됩니다.
  - 분산된 여러 에이전트 그룹이 공통의 신뢰 기준(Shared Ground Rules)을 유지할 수 있도록 만듭니다.

## 🔗 연결된 문서
- [[wiki/Agents/Implementation/000_Implementation-MOC.md]]
- [[wiki/Agents/Implementation/Deep-Agents-Architecture-Patterns.md]]
- [[wiki/Business/Trends/AI-시대의-기업-미래와-토큰-자본-전략.md]]
- [[index.md]]
