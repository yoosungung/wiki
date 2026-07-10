---
title: "torch-rbln: 리벨리온 NPU를 위한 PyTorch 네이티브 개발 환경"
related_raw: ["[[2026-05-12-SqueezeBits_Introducing_ATOM_Max.md]]"]
tags: ["Engineering/Development-Environment", "Rebellions", "PyTorch", "NPU", "Eager-Mode"]
date: "2026-05-12"
---

# torch-rbln: 리벨리온 NPU의 PyTorch 네이티브 통합

## 1. 개요
`torch-rbln`은 리벨리온 NPU 연산을 PyTorch 워크플로우에 직접 통합하기 위한 익스텐션입니다. 기존의 명시적 컴파일 및 내보내기(Export) 단계를 줄이고, GPU와 유사한 개발 경험을 제공하는 것을 목표로 합니다.

## 2. 핵심 기술: PrivateUse1 디스패처
- PyTorch의 **PrivateUse1** 메커니즘을 활용하여 리벨리온 전용 커널을 등록합니다.
- 이를 통해 PyTorch 자체를 수정하지 않고도 리벨리온 NPU를 가속 장치로 인식하게 합니다.

## 3. 주요 모드
1. **Eager Mode**:
    - 정의-실행(Define-by-run) 방식으로 개별 연산을 NPU에서 즉시 실행합니다.
    - 디버깅, 신속한 프로토타이핑 및 대화형 개발에 유리합니다.
2. **torch.compile (TorchDynamo) 통합**:
    - `backend="rbln"` 설정을 통해 그래프 수준의 최적화 및 JIT 컴파일을 지원합니다.
    - 모델 내보내기 과정 없이 PyTorch 코드 내에서 직접 하드웨어 가속을 트리거합니다.

## 4. 도입 효과
- **개발 생산성 향상**: 모델 수정 후 매번 컴파일할 필요가 없어 실험 및 디버깅 주기가 단축됩니다.
- **vLLM과의 시너지**: vLLM의 고수준 서빙 로직(스케줄링, 텐서 병렬성 등)을 PyTorch 네이티브 코드로 직접 활용할 수 있어 유지보수가 용이해집니다.
- **하이브리드 실행**: NPU에서 지원하지 않는 연산은 호스트 CPU로 폴백(Fallback)하여 실행을 유지하면서, 가능한 연산은 NPU에서 가속하는 유연한 전략 수립이 가능합니다.

---
**관련 문서**:
- [[wiki/Engineering/Infrastructure-and-DevOps/Rebellions-Software-Stack.md]]
- [[wiki/Models/Architectures/Rebellions-ATOM-Max.md]]
