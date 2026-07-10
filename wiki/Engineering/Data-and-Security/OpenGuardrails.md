---
title: "OpenGuardrails"
related_raw: ["[[wiki/Engineering/Data-and-Security/OpenGuardrails.md]]"]
tags: ['wiki', 'engineering_and_infra', 'dev_environment']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# OpenGuardrails

Kalyan KS는 LinkedIn 게시물에서 LLM(대규모 언어 모델) 애플리케이션을 보호하기 위한 개발자 우선 오픈소스 AI 보안 플랫폼인 **OpenGuardrails**를 소개합니다. OpenGuardrails는 다음과 같은 주요 기능을 제공합니다:

*   **프롬프트 인젝션 방어:** 탈옥(jailbreaks), 프롬프트 인젝션, 코드 인터프리터 남용 및 악성 코드 생성 시도로부터 보호합니다.
*   **데이터 유출 방지:** NER(개체명 인식) 파이프라인 및 정규식 기반 탐지를 사용하여 민감한 개인 및 조직 정보를 식별하고 수정합니다.
*   **콘텐츠 안전 감지:** 12가지 위험 범주에 걸쳐 유해하거나 혐오스럽거나 불법적이거나 성적으로 노골적인 콘텐츠를 구성 가능한 민감도 임계값으로 감지합니다.

OpenGuardrails의 주요 특징은 다음과 같습니다:

*   **통합 LLM 아키텍처:** 콘텐츠 안전 및 모델 조작 감지를 모두 처리하는 단일 14B→3.3B (GPTQ 양자화) 모델을 사용하며, 프로덕션 수준의 효율성을 유지하면서 우수한 의미론적 이해를 제공합니다.
*   **다국어 우수성:** 119개 언어 및 방언에서 강력한 성능을 제공하며, 영어, 중국어 및 다국어 벤치마크에서 SOTA(State-Of-The-Art) 결과를 달성했습니다.
*   **프로덕션 준비 플랫폼:** 대규모 안전 LLM과 배포 가능한 플랫폼을 모두 갖춘 최초의 완전 오픈소스 가드레일 시스템입니다. RESTful API, Docker 배포 및 모듈식 구성 요소를 통해 원활한 비공개/온프레미스 통합을 지원합니다.

**관련 URL:**
*   OpenGuardrails GitHub 저장소: `https://github.com/openguardrails/openguardrails`

[출처](https://www.linkedin.com/posts/kalyanksnlp_llms-guardrails-aiengineers-activity-7396395268595699712-vpbm?utm_source=share&utm_medium=member_ios&rcm=ACoAADm5eyABU_duDuXv1f9N-6JhXB_iNO6faes)