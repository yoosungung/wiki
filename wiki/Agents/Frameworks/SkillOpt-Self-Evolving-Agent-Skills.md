---
title: "SkillOpt: 에이전트 자율 진화(Self-Evolving) 스킬 최적화 프레임워크"
tags: ["Agents", "Frameworks", "SkillOpt", "Self-Evolution", "Optimization", "Claude-Code"]
type: "wiki"
status: "published"
last_updated: "2026-06-21"
related_raw: ["[[2026-06-21-microsoft-skillopt-readme.md]]"]
---

# 🛠️ SkillOpt: 에이전트 자율 진화 스킬 최적화 프레임워크

**SkillOpt**는 마이크로소프트(Microsoft)에서 2026년 6월 오픈소스로 공개한 에이전트 스킬 최적화 프레임워크입니다. LLM 에이전트의 프롬프트나 스킬 문서(Skill Document)를 **동결된(Frozen) 에이전트 모델의 학습 가능한 가중치(Trainable State)**로 취급하여, 가중치 업데이트 없이 텍스트 영역에서 딥러닝 옵티마이저의 규율(Epochs, Mini-batch, Learning Rate, Validation Gate)을 적용하여 자율적으로 진화시킵니다.

---

## 1. 핵심 개념 및 아키텍처

기존의 에이전트 프롬프트 튜닝이나 스킬 진화 방식은 개발자가 수동으로 작성하거나, LLM이 일회성(One-shot)으로 생성하거나, 혹은 통제되지 않은 자가 수정을 거쳤기 때문에 피드백 하에 확실한 성능 향상을 보장하기가 어려웠습니다. SkillOpt는 이를 보완하기 위해 다음과 같은 심층 학습 메커니즘을 텍스트 영역에 모사합니다.

1. **텍스트 공간 내 최적화 (Text-Space Optimization)**:
   - 스킬 명세서 자체를 최적화할 파라미터 상태로 정의합니다.
   - 별도의 **옵티마이저 모델**을 두어 에이전트의 롤아웃(Rollout) 실행 점수 및 로그 피드백을 기반으로, 기존 스킬 문서에 대한 삽입(Add), 삭제(Delete), 대체(Replace) 경계를 판단하는 가감 편집을 수행합니다.
2. **검증 게이트 (Validation Gate)**:
   - 편집된 후보 스킬이 검증 데이터셋(Validation Split) 상에서 기준 점수 이상의 성능 향상을 보였을 때만 상태 업데이트를 허용(Accept)합니다. 이를 통해 무작위 에러나 오버피팅 없이 스킬이 안정적으로 우상향 발전하도록 통제합니다.
3. **훈련 루프 파이프라인**:
   - `Rollout (실행)` ➔ `Reflect (반성)` ➔ `Aggregate (취합)` ➔ `Select (선택)` ➔ `Update (갱신)` ➔ `Evaluate (평가)` 단계를 거치며 반복 학습을 수행합니다.

---

## 2. 주요 기능 및 생태계 (2026.06 업데이트)

*   **다양한 LLM 백엔드 지원**: OpenAI, Azure, Claude, Qwen, MiniMax 등 이종 모델 API 레이어 결합을 공식 지원합니다.
*   **WebUI 대시보드 제공**: 스킬 학습 현황과 롤아웃 점수의 변동 추이를 실시간 모니터링할 수 있는 대시보드가 패키지에 내장되어 있습니다.
*   **SkillOpt-Sleep (2026-06-15 프리뷰 출시)**:
   - **야간 자율 진화(Self-Evolution) 동반자 기능**입니다.
   - Claude Code, Codex, Copilot과 같은 로컬 코딩 에이전트와 연동하여 에이전트가 주간에 수행한 코딩 세션 이력을 바탕으로 밤(오프라인 시간) 동안 과거 기록을 검토하고, 반복 오류가 나는 지점을 스스로 재생(Replay)하며 스킬 문서를 보완합니다. 검증 게이트를 통과한 결과물만을 차기 세션 스킬(`best_skill.md`)로 릴리즈합니다.
*   **타 에이전트 생태계 통합**:
   - 2026년 6월 초 기준 `gbrain`, `gbrain-evals`, `darwin-skill` 등의 주요 자율 에이전트 평가 및 실행 생태계에 SkillOpt가 공식 통합되었습니다.

---

## 3. 설치 및 활용 방법
PyPI에 공식 등록되어 간단하게 설치할 수 있습니다:
```bash
pip install skillopt
```
이후 `skillopt train --config config.yaml` 명령을 통해 사전에 정의된 시나리오와 검증 기준하에 에이전트 스킬 진화 훈련을 실행합니다.

---

**관련 문서**:
- [[wiki/Agents/Frameworks/000_Frameworks-MOC]]
- [[wiki/Agents/Frameworks/차세대-자율-수행-에이전트-분석-2026]]
