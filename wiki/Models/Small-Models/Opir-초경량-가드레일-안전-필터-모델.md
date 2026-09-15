---
title: Opir 초경량 가드레일 안전 필터 모델
tags: ["Models", "Small-Models", "Guardrails", "Safety", "GLiClass"]
type: wiki
status: published
created: 2026-07-05
updated: 2026-07-05
related_raw: ["[[2026-07-05-opir_lightweight_sota_guardrail_models_gliclass.md]]"]
---

# Opir 초경량 가드레일 안전 필터 모델

**Opir**는 실시간 대화형 서비스나 온디바이스 에이전트 구동 환경에서 유해 프롬프트, 악성 및 독성 대화(toxic language), 탈옥 시도(jailbreak) 등을 실시간 차단하도록 설계된 초경량 인코더(Encoder) 기반 가드레일 보안 필터 모델군입니다.

## 1. 개발 배경 및 필요성
기존 Llama Guard나 Guardrails 관련 도구들은 대형 LLM 백본을 사용해 추론 오버헤드와 응답 레이턴시를 심각하게 가중시켰습니다. Opir는 이러한 서빙 지연 문제를 방지하기 위해 100M 미만의 극단적인 경량화를 달성했습니다.

## 2. 주요 기술적 특징

1. **초저지연(Sub-30ms) 응답 속도**
   - 일반 인코더 변형 모델의 경우 p50 레이턴시가 **30ms 미만**으로 동작합니다.
   - 스마트폰이나 에지 기기 상에서 구동되는 극소형 Edge 모델의 경우 **10ms 이하**의 즉각적인 응답성을 보장하여 API 콜 차단의 병목을 제거합니다.
2. **GLiClass 아키텍처 기반**
   - 제로샷(Zero-shot) 및 퓨샷(Few-shot) 텍스트 분류 성능이 우수한 **GLiClass** 기술을 채택하여, 사전에 정의되지 않은 유동적인 위협 카테고리나 공격 기법에 대해서도 유연하고 강건한 분류 성능을 보여줍니다.
3. **엣지 및 온디바이스(On-device) 최적화**
   - 100M 미만의 파라미터 크기 덕분에 저성능 하드웨어나 모바일 NPU 가속 환경에서도 부담 없이 백그라운드 필터링 시스템으로 상시 기동(Always-on)이 가능합니다.

## 관련 문서
- [[wiki/Models/Small-Models/000_Small-Models-MOC.md]]
- [[wiki/Models/Small-Models/GLiNER-Lightweight-Entity-Extraction.md]]
- [[wiki/Models/Small-Models/GLiNER2-PII-Detection-Model.md]]
- [[wiki/Models/Optimization-and-Serving/OpenGuardrails_LLM_앱_보호_오픈소스_AI_보안_플랫폼.md]]
