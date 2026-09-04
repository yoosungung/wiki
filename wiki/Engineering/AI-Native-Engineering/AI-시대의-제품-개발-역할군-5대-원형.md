---
title: AI 시대의 제품 개발 역할군 5대 원형
tags: ["Engineering", "AI-Native", "Team-Structure", "Anthropic"]
type: wiki
status: published
last_updated: "2026-09-04"
updated: "2026-09-04"
related_raw: ["[[2026-07-05-future_product_roles_archetypes_anthropic.md]]", "[[2026-09-04-the-end-of-software-engineering-intent-architect-aaas.md]]"]
---

# AI 시대의 제품 개발 역할군 5대 원형 (Future Product Roles)

AI 코딩 에이전트(Claude Code 등)와 생성형 AI 기술이 개발 프로세스 전반에 통합됨에 따라, 엔지니어링, 디자인, 기획, 데이터 분석의 경계가 무너지고 있습니다. Anthropic의 Claude Code 팀 운영 방식을 참고하여 정립한 미래 제품 개발 조직의 5대 역할 원형(Archetypes)입니다.

## 1. 5대 역할군 정의 (The 5 Archetypes)

이 역할들은 전통적인 타이틀(예: 프론트엔드 개발자, 디자이너, PM)에 종속되지 않으며, 한 명의 조직원이 2~3개 역할을 교차하여 수행할 수도 있습니다.

1. **Prototyper (프로토타이퍼)**
   - **역할**: 새로운 아이디어를 검증하기 위해 빠르고 민첩하게 작동하는 프로토타입을 대량으로 제작합니다.
   - **특징**: "신속한 파기(Fail Fast)"를 전제로 하며, 대다수의 작업물이 실제 프로덕션 빌드에 도달하지 않더라도 기획의 폭을 넓히는 데 기여합니다.
2. **Builder (빌더)**
   - **역할**: 검증된 프로토타입이나 제품 스펙을 실서비스 수준의 견고한 프로덕션 코드 및 인프라로 전환합니다.
   - **특징**: 에이전트를 효율적으로 조종하고 시스템의 안전성과 코드 품질을 보장합니다.
3. **Sweeper (스위퍼)**
   - **역할**: 코드베이스와 시스템 설계를 청소하고 단순화합니다. 불필요한 기능 제거(Unshipped), UI 개선, 리팩토링, 성능 최적화를 전담합니다.
   - **특징**: 복잡도를 엄격히 통제하여 에이전트의 컨텍스트 윈도우 부하 및 실행 토큰 비용을 최소화하는 핵심적인 역할을 합니다.
4. **Grower (그로워)**
   - **역할**: 배포된 제품을 바탕으로 데이터 분석과 사용자 피드백을 수집하며, 이터레이션을 반복해 PMF(Product-Market Fit)를 극대화합니다.
5. **Maintainer (메인테이너)**
   - **역할**: 대규모 트래픽 하에서도 성숙한 서비스가 안전하고, 빠르며, 효율적으로 작동하도록 인프라 신뢰성과 보안 거버넌스를 책임집니다.

## 2. 제품 단계별 조직 구성 전략

단일 스택 제품 개발 하에서는 제품의 수명 주기에 맞춰 필요한 원형의 배율이 조정됩니다.

- **Pre-PMF (초기 빌딩) 단계**: 1 (Prototyper) + 2 (Builder) + 3 (Sweeper) 중심의 빠른 스피드와 간소화가 핵심.
- **Growth (성장) 단계**: 2 (Builder) + 3 (Sweeper) + 4 (Grower) 및 일부 5 (Maintainer) 결합.
- **Mature (안정화) 단계**: 3 (Sweeper) + 4 (Grower) + 5 (Maintainer) 중심의 운영 효율화 및 신뢰성 유지.

## 관련 문서
- [[wiki/Engineering/AI-Native-Engineering/000_AI-Native-Engineering-MOC.md]]
- [[wiki/Engineering/AI-Native-Engineering/The-End-of-Software-Engineering-Intent-Architecture.md|소프트웨어 공학의 종말: 인텐트 아키텍트]]
- [[wiki/Engineering/AI-Native-Engineering/Claude-Code-and-Cursor-AI-Native-Engineering-에이전트-기반-엔지니어링.md]]
- [[wiki/Agents/Coding-and-Engineering/000_Coding-and-Engineering-MOC.md]]
