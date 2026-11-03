---
title: "LLM 사후학습(Post-Training) 심층 분석: OPD 역학, 희소 보상 기아, 자가 학습 검증 (2026)"
date: "2026-11-03"
last_updated: "2026-11-03"
updated: "2026-11-03"
tags: ["Models", "RL", "OPD", "Distillation", "GRPO", "Self-Training", "Post-Training", "SRD", "DARA"]
related_raw: ["[[2026-11-03-Post-Training-OPD-Sparse-Rewards-Review-2026.md]]"]
type: "wiki"
---

# LLM 사후학습(Post-Training) 심층 분석: OPD 역학, 희소 보상 기아, 자가 학습 검증 (2026)

## 1. 핵심 요약 (Executive Summary)
2026년 8~10월 발표된 주요 LLM 사후학습(Post-Training) 연구 16편을 종합하면, 기존의 통념(교사 지식 전이로서의 증류, GRPO 만능주의, 단일 자기평가 기반 자가 진화, 무제한 샘플링 확장)을 뒤집는 **5가지 구조적 메커니즘**이 규명되었다.
1. **온폴리시 증류(OPD)의 실체**: OPD의 성능 향상은 교사 모델의 지식을 배운 결과가 아니라 **학생이 낮은 확률로 선택하던 노이즈 토큰을 억제한 효과**가 주원인이다.
2. **장기 워크플로 희소 보상 기아(Sparse Reward Starvation)**: 전체 대화의 `3.4%`에서만 발동하지만 점수를 `+0.455` 끌어올리는 결정적 능력(장기 기억 호출 등)은 대부분 그룹에서 보상 분산이 0이 되어 표준 [[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md|GRPO]]로 학습되지 않는다. 이를 해결하기 위해 **SRD**(사후 실패의 사전 주의사항 변환)와 **DARA**(밀도 인지 다중 보상 가중치)가 도입되었다.
3. **자가 학습 공조 부정행위(Co-Cheating) 차단**: 생성·풀이·채점 루프에서 동일 오류가 누적되는 현상을 막기 위해 **데이터 분할 교차 검증(False Frontiers)** 및 **10% 실환경(원본 파일·코드 실행) 그라운딩**이 필수적이다.
4. **에이전트 후보 생성 vs 선택 병목(Mid-Harness)**: 에이전트는 정답 명령을 이미 후보군에 생성해 두고도 선택하지 못해 실패하며, 메모리 태그(`memory`) 표기 방식만으로도 사용 빈도가 `10~14%p` 왜곡된다.
5. **샤프닝 택스(Sharpening Tax)**: 사후학습(RL/SFT)은 기존 가능 풀이의 적중률은 높이지만 새로운 해법 탐색 다양성을 깎아먹으므로, 어려운 문제에만 선택적으로 탐색을 늘리거나 서로 다른 체크포인트를 앙상블해야 한다.

---

## 2. 영역별 핵심 메커니즘 및 설계 패턴

### 2.1 온폴리시 증류(OPD)와 파라미터 업데이트 방향성
- **교사 없는 자기 개선 (*Does On-Policy Distillation Really Distill?*)**:
  - [[wiki/Models/RL/LMSYS-Miles-On-Policy-Distillation.md|On-Policy Distillation (OPD)]]이 성능을 높이는 핵심 원인은 교사(Teacher)의 지식을 흡수해서가 아니라, **학생 모델이 원래 낮은 확률로 선택했던 불안정 토큰들을 후속 스텝에서 덜 쓰도록 억제(Token Suppression)**했기 때문이다. 실제로 교사 모델을 완전히 제거하고 저확률 선택 토큰만 억제해도 기존 OPD보다 높은 성능이 달성된다.
- **Forward vs Reverse KL의 지배력 (*On-Policy or Off-Policy Learning?*)**:
  - 롤아웃을 학생이 생성했는지(On-policy) 교사가 생성했는지(Off-policy)보다, 목적 함수로 **Forward KL과 Reverse KL 중 무엇을 사용하는지**가 과제 성능을 훨씬 크게 좌우한다.
- **표현 잔차 및 파라미터 방향 재사용 (*The Teacher Is a Direction, Not a Destination* / *On-Policy Parameter Update Direction*)**:
  - RL이나 OPD가 은닉 상태(Hidden State)나 가중치 파라미터를 변화시킨 **방향 벡터(Update Direction)**만 추출하여 후속 학습에 외삽·재사용해도 일반화 성능이 향상된다. 단, 이 방향 벡터를 얻기 위해 선행 RL/OPD가 필요하다는 연산 비용 한계가 존재한다.

### 2.2 장기 워크플로 희소 보상 기아와 SRD · DARA
- **GRPO의 희소 능력 학습 실패 (*RealCompanion*)**:
  - 장기 대화에서 사용자가 과거에 언급한 계획·고민을 적시에 연결해야 하는 상황은 전체 대화의 **3.4%**에 불과하지만, 정확히 인출해 답하면 응답 품질 점수가 **+0.455점** 급등한다.
  - 그러나 96.6%의 일반 롤아웃 그룹에서는 과거 대화 참조 여부에 따른 보상 차이가 `0`이므로, 그룹 내 상대 비교를 수행하는 GRPO에서는 학습 신호가 소멸한다.
- **SRD (*Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight*)**:
  - 그룹 내 모든 풀이가 실패했더라도 반복된 실수 패턴을 추출하여, 다음 문제를 풀기 전 **사전 주의사항(Prior Foresight)**으로 주입해 증류함으로써 희소 보상 구간의 학습 정체를 돌파한다([[wiki/Models/RL/RLTLDR-Self-Generated-Feedback-Internalization.md|RLTL;DR]]과 상호 보완).
- **DARA (*Make Sparse Rewards Count: Density-Aware Reward Aggregation*)**:
  - 다중 평가 기준(정답률, 포맷, 길이 등)을 결합할 때, 롤아웃 간 변별 빈도가 낮아 묻히기 쉬운 희소 기준에 **밀도 반비례 가중치**를 동적으로 부여하여 형식·길이·제약 조건이 학습에서 무시되지 않게 보장한다([[wiki/Models/RL/GD2PO-Multi-Reward-Conflict-Mitigation.md|GD²PO]] 참조).

### 2.3 자가 진화(Self-Training)의 공조 오류(Co-Cheating)와 교차 검증
- **False Frontiers (*Diagnosing and Mitigating Co-Cheating in Self-Evolving Search Agents*)**:
  - 모델이 스스로 문제를 만들고 풀고 채점하는 자기 학습 루프에서는 동일한 논리 오류가 생성기·풀이기·채점기에 공명(Co-cheating)하여 학습할수록 성능이 하락([[wiki/Models/Architectures/Model-Collapse-Recursive-Synthetic-Data-Degradation.md|모델 붕괴]])한다.
  - **해법**: 평가용 Solver들을 **서로 다른 데이터 분할(Split)**로 독립 학습시킨 뒤, 각자 학습하지 않은 영역의 질문에 대해 상호 동의(Cross-check)하는지 검증한다. 이를 통해 7개 검색 벤치마크 평균 정답률을 기존 Self-training 대비 **+8%p 이상** 향상시켰다.
- **10% 실환경 그라운딩 (*GraphForge* / *Scaling Automatic Research Agents via World Models*)**:
  - 모델의 자기평가만 믿지 않고 전체 학습 자료의 **약 10%만이라도 원본 파일 대조나 실제 코드 실행 결과로 교차 검증**하면 자가 학습 드리프트가 억제되고 성능이 크게 상승한다.
- **검증기 다양성 원칙 (*Questioning the Questions* / *Nemotron IMO Gold Recipe*)**:
  - 동일한 학습 경로를 공유하는 여러 Verifier가 만장일치를 이루더라도 같은 논리적 맹점을 동시에 놓칠 수 있다. 단순 Verifier 개수 증설보다 **서로 다른 정보 원천과 학습 경로를 가진 이종 검증기(Heterogeneous Verifiers)**를 결합하는 것이 핵심이다.

### 2.4 에이전트 행동 선택(Mid-Harness) 및 샤프닝 택스(Sharpening Tax)
- **후보 생성보다 선택이 병목 (*Mid-Harness: Scaling Actions Between Model and Harness for Terminal Agents*)**:
  - 터미널 에이전트가 실패하는 주원인은 올바른 셸 명령을 생성하지 못해서가 아니라, **이미 생성한 후보 명령들 중에서 정답을 고르지 못하기 때문**이다. 강력한 Verifier가 후보 중 적절한 명령만 선택해 주어도 터미널 태스크 성공률이 대폭 상승한다.
- **메모리 라벨 편향 (*Hi-Q* / *RealCompanion*)**:
  - 다단계 검색과 장기 대화에서는 현재 근거로 즉시 답할지 추가 검색할지 먼저 판단해야 한다. 특히 동일한 텍스트라도 프롬프트에 `memory`라는 태그로 표시하면 모델이 내용을 불문하고 **10~14%p 더 자주 인용**하는 표시 편향(Label Bias)이 발생하므로 프롬프트 설계 시 주의해야 한다.
- **샤프닝 택스 (*Sharpening Tax in Post-Training*)**:
  - RL이나 Instruction Tuning을 거치면 원래 풀 수 있던 문제의 안정성은 높아지지만(분포 첨예화), 틀린 문제에서 완전히 새로운 해법을 탐색하는 엔트로피는 감소한다. 따라서 쉬운 문제에 샘플링을 낭비하지 말고 **고난도 문제에만 탐색 예산을 집중하거나 서로 다른 체크포인트를 혼합(Checkpoint Mixing)**하는 전략이 우월하다.

---

## 3. 참고 논문 목록 (16 Core Papers, 2026.08–2026.10)
1. *Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement* (2026-08)
2. *Hi-Q: Hierarchical Evidence-guided Query Refinement for Multi-Hop Question Answering* (2026-08)
3. *The Teacher Is a Direction, Not a Destination: Extrapolating RL-Induced Representation Residuals in On-Policy Distillation* (2026-09)
4. *False Frontiers: Diagnosing and Mitigating Co-Cheating in Self-Evolving Search Agents* (2026-09)
5. *RealCompanion: Benchmarking Human Understanding from Reasoning over Longitudinal Real-World Conversations* (2026-10)
6. *On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics* (2026-09)
7. *GraphForge: Training Working Agents with Graph-Anchored Workspace Synthesis* (2026-09)
8. *Mid-Harness: Scaling Actions Between Model and Harness for Terminal Agents* (2026-09)
9. *Sharpening Tax in Post-Training* (2026-10)
10. *On-Policy Parameter Update Direction Underlies Generalization in LLM Post-Training* (2026-09)
11. *Questioning the Questions: Sustaining Self-Evolution in Reasoning Models* (2026-10)
12. *LexReward: A Taxonomy-Driven Reward Framework for Legal Language Models* (2026-09)
13. *Make Sparse Rewards Count: Density-Aware Reward Aggregation for Multi-Reward RL (DARA)* (2026-10)
14. *Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight (SRD)* (2026-10)
15. *Scaling Automatic Research Agents via World Models* (2026-08)
16. *An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics* (2026-09)

---

## 4. 관련 문서 (Cross-References)
- [[wiki/Models/RL/LMSYS-Miles-On-Policy-Distillation.md]]
- [[wiki/Models/RL/RLTLDR-Self-Generated-Feedback-Internalization.md]]
- [[wiki/Models/RL/GD2PO-Multi-Reward-Conflict-Mitigation.md]]
- [[wiki/Models/RL/DeepSeek-R1-GRPO-Implementation.md]]
- [[wiki/Models/Architectures/Model-Collapse-Recursive-Synthetic-Data-Degradation.md]]
- [[wiki/Models/RL/000_RL-MOC.md]]
