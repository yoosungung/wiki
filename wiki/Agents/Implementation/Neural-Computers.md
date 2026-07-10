---
title: "Neural Computers (NCs) & Completely Neural Computers (CNCs)"
tags: ["Neural-Computers", "CNC", "Architectures", "Agentic-OS", "Future-Computing"]
related_raw: ["[[raw/ai computer.md]]", "[[raw/2026-04-25-research-ingest-t2sql-osi-mcp.md]]"]
---

# Neural Computers (NCs): 새로운 컴퓨팅 패러다임

## 1. 개요
**Neural Computers (NCs)**는 전통적인 컴퓨터의 연산(Computation), 메모리(Memory), 입출력(I/O)을 하나의 학습된 런타임 상태(Learned Runtime State)로 통합하는 새로운 프론티어를 제안합니다. (arXiv:2604.06425, 2026.04)

이 연구는 기존의 에이전트나 전통적인 컴퓨터 시스템을 넘어선 **Completely Neural Computer (CNC)**를 최종 목표로 합니다.

## 2. 핵심 개념
- **CNC (Completely Neural Computer)**: 성숙하고 범용적인 형태의 신경망 기계로, 안정적인 실행, 명시적 프로그래밍(Explicit Reprogramming), 영구적인 기능 재사용(Durable Capability Reuse)이 가능한 형태입니다.
- **Unified Runtime**: 프로그램의 상태, 데이터, 입출력이 별도의 하드웨어 레이어 없이 신경망의 가중치와 활성화 상태 내에서 일체형으로 처리됩니다.

## 3. 연구 현황 및 실증 (2026.04)
NC의 기초 프리미티브를 학습하기 위해 연구진은 비디오 모델을 활용하였습니다:
- **I/O Trace 기반 학습**: 별도의 프로그램 상태 정보 없이, 수집된 입출력 트레이스(Trace)만으로 NC 프리미티브를 학습할 수 있는지 탐구.
- **Video Model 기반 구현**: 명령어(Instructions), 픽셀, 사용자 행동을 입력받아 화면 프레임을 생성(Roll out)하는 비디오 모델로 NC를 인스턴스화함.
- **성과**: CLI 및 GUI 환경에서 기초적인 인터페이스 프리미티브(입출력 정렬, 짧은 호라이즌 제어) 습득에 성공.

## 4. 한계 및 향후 과제
- **Symbolic Stability**: 기호 수준의 안정성을 확보하는 것이 여전히 도전 과제임.
- **Routine Reuse**: 학습된 루틴을 효율적으로 재사용하고 제어된 업데이트를 수행하는 능력이 아직 미흡함.
- **Roadmap**: CNC로 나아가기 위해 기호적 안정성과 내구성 있는 역량 재사용을 해결하기 위한 로드맵 제시.

## 5. AX1센터 R&D 시사점
- **AI-Native Engineering**: 기존 OS의 추상화 레이어를 거치지 않고 직접 UI/UX를 제어하거나 연산 로직을 수행하는 '완전 신경망 OS'의 가능성 시사.
- **비디오 기반 에이전트**: 화면 자체를 연산의 결과물로 생성하는 멀티모달 에이전트 설계 시 NC의 프레임워크를 참고할 수 있음.

## 참고 자료
- [Neural Computers (arXiv:2604.06425)](https://arxiv.org/abs/2604.06425) - Mingchen Zhuge, Jürgen Schmidhuber et al.
- GitHub: `metauto-ai/NeuralComputer`
- Blog: `metauto.ai/neuralcomputer`

## 관련 문서
- [[wiki/Agents/Implementation/AI OS.md]]
- [[wiki/Models/Multimodal-and-Vision/000_Multimodal-MOC.md]]
