---
title: "Google-RT-3-Open-Source-Robotics"
related_raw: ["[[wiki/Agents/Robotics-and-VLA/Google-RT-3-Open-Source-Robotics.md]]"]
tags: ['wiki', 'agents_and_systems', 'robotics_&_physical_ai_(vla)']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# Google RT-3: 오픈소스 기반 범용 로보틱스 트랜스포머

### 1. 개요 및 핵심 컨셉
Google은 자사의 최신 로보틱스 파운데이션 모델인 **RT-3 (Robotics Transformer 3)**를 전격 오픈소스로 공개했습니다. RT-3는 다양한 형태의 로봇 하드웨어에 즉시 적용 가능한 범용성을 갖추고 있으며, 시각-언어-행동(VLA)을 하나의 트랜스포머 구조로 통합하여 복잡한 지시사항을 물리적 행동으로 변환하는 능력이 탁월합니다.

### 2. 주요 기술 세부 사항
- **Cross-Robot Transfer Learning:** 서로 다른 제조사의 로봇 팔이나 이동형 로봇에서 수집된 데이터를 통합 학습하여, 한 로봇에서 배운 기술을 다른 로봇으로 전이시킬 수 있습니다.
- **Tokenized Action Space:** 로봇의 모든 관절 움직임과 그리퍼 조작을 언어 토큰처럼 처리하여, LLM이 문장을 생성하듯 정교한 행동 시퀀스를 생성합니다.
- **Low-Latency Inference:** 실시간 물리 상호작용을 위해 추론 지연 시간을 획기적으로 낮추어, 사람의 돌발 행동에도 즉각적으로 대응할 수 있습니다.

### 3. 관련 기술 URL 및 리소스
- [Google DeepMind RT-3 Blog](https://deepmind.google/discover/blog/rt-3/)
- [RT-3 GitHub Repository](https://github.com/google-research/robotics-transformer)
- [VLA-Adapter for RT-3 Training](https://example.com/vla-adapter)

### 4. 설명 이미지 추출 (Conceptual)
- ![RT-3 Architecture](https://example.com/rt3-arch.png) (VLA 통합 모델 구조도)
- ![Robot Task Execution](https://example.com/rt3-tasks.png) (주방 보조, 물건 정리 등 실제 수행 사례)

### 5. 관련 노트 링크
- [[wiki/Agents/Frameworks/구글의-Embodied-Agent-SIMA]]
- [[wiki/Agents/Frameworks/구글의-LLM-기반-에이전트-한계-고백]]
- [[wiki/Business/2026년-로봇-공학-예측]]
