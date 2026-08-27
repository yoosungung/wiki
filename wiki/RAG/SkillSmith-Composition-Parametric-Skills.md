---
title: "SkillSmith Composition Parametric Skills"
tags: ['#inbox', '#RAG', '#SkillSmith']
type: "wiki"
status: "published"
---

# SkillSmith Composition Parametric Skills

## 핵심 요약
SkillSmith는 모델이 보유한 텍스트 기반 지식과 매개변수화된 스킬(Parametric Skills)을 효과적으로 합성하여 추론 능력과 제로샷 학습(Zero-Shot)을 개선하는 연구 또는 아키텍처 방법론입니다.

## 주요 성과 (Metrics & Claims)
Super-Natural Instructions(SNI) 및 MMLU-ProX 등의 다양한 벤치마크 평가 결과에서 SkillSmith는 기본(Base) 모델의 직접 학습 및 기존 특이값 분해(SVD) 기법 등과 비교하여 우수한 결과를 보여주었습니다.

- **SNI(Super-Natural Instructions) 결과**: 
  - 검색된 SkillSmith 기법 적용 시 NLL(음의 로그 우도) 수치가 획기적으로 낮아져, 기존 LERP나 SVD 기법보다 향상된 제로샷(Zero-shot) 및 다운스트림 Fine-Tuning 능력을 입증했습니다.
- **MMLU-ProX 다국어/복합 과제 개선**:
  - 기존 모델들이 어려움을 겪는 복합 추론(Indonesian Law, Zulu Physics 등)에서 NLL 지표가 지속적으로 하락(성능 향상)하며 안정적인 성능을 유지했습니다.

> **참고**: 이 데이터는 기존 지식 구조화 방식 대비, Parametric Skill을 다루는 향상된 접근법이 모델의 범용적인 과제 해결 및 파인튜닝 비용 감소에 크게 기여할 수 있음을 나타냅니다.
