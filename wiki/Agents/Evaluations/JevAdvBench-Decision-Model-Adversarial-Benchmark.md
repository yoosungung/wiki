---
title: "JevAdvBench 및 결정·자가개선 모델 평가 감사: RLCD 적대적 공격, LettuceDetect, RSI 벤치마크 함정"
date: "2026-11-03"
last_updated: "2026-11-03"
updated: "2026-11-03"
tags: ["Agents", "Evaluations", "JevAdvBench", "RLCD", "Decision-Models", "Adversarial-Robustness", "LettuceDetect", "Hallucination", "Benchmark-Audit"]
related_raw: ["[[2026-11-03-JevAdvBench-Adversarial-Benchmark-RLCD.md]]", "[[2026-11-03-Jeva-Robust-Decision-Model.md]]"]
type: "wiki"
---

# JevAdvBench 및 결정·자가개선 모델 평가 감사: RLCD 적대적 공격, LettuceDetect, RSI 벤치마크 함정

## 1. 핵심 요약 (Executive Summary)
에이전트 라우팅·승인·평가를 담당하는 결정 모델(RLCD: Reinforcement Learning for Calibrated Decisions)과 자가 개선(RSI) 모델이 프로덕션에 투입됨에 따라, 이들의 **적대적 취약점(Adversarial Vulnerability)**과 **벤치마크 검증 무결성(Evaluation Integrity)**을 감사하는 3대 핵심 프레임워크 및 방법론이 정립되었다.
1. **`JevAdvBench`**: Jev 스타일 RLCD 결정 모델을 겨냥한 최초의 적대적 벤치마크(66개 시나리오, 812개 타입 질문, 9,744개 단일 편집 블랙박스 변이)로, **검증되지 않은 의견 한 줄 추가만으로 결정의 12.1%가 뒤집히고 고신뢰 응답의 38%가 인간 검토 임계값(0.8) 아래로 추락**함을 실증했다.
2. **`LettuceDetect`**: RAG 파이프라인에서 문맥에 근거하지 않은 환각 구간을 **토큰 단위(Token-level span)**로 색출하는 ModernBERT(4K 컨텍스트, RAGTruth 학습, MIT 라이선스) 기반 초경량 오픈소스 탐지기다.
3. **자가 개선 모델(`Darwin 27B RSI`) 벤치마크 감사 원칙**: 공개 레시피 없는 자가 채점(Self-grading) 주장과 평가 프로토콜 불일치(단일 샘플 vs 재시도+검증 패스 간 14%p 격차)를 식별하는 엔터프라이즈 모델 검증 기준을 제시한다.

---

## 2. `JevAdvBench`: RLCD 결정 모델의 적대적 강건성 평가

### 2.1 왜 기존 LLM 적대적 벤치마크로는 결정 모델을 평가할 수 없는가?
- 기존 적대적 벤치마크(Jailbreak, Prompt Injection)는 모델이 생성한 유해 텍스트나 잘못 실행한 도구 호출을 채점한다.
- 반면 RLCD 결정 모델([[wiki/Agents/Frameworks/TypeSafe-Jev-System-One-Decision-Architecture.md|Jev]], [[wiki/Models/Optimization-and-Serving/AnyJev-and-Jeva-Decision-Model-Ecosystem.md|AnyJev/Jeva]])은 텍스트를 전혀 생성하지 않고, 공격자에게 조작당한 상태에서도 **문법적으로 완벽한 타입 결정(확률·선택·점수)**만 조용히 반환하므로 기존의 출력 기반 필터로는 피격 여부를 탐지할 수 없다.

### 2.2 벤치마크 구조 및 핵심 실험 결과
- **데이터셋 규모**: **66개 도메인 시나리오**, **812개 타입화된 질문(Typed Questions)**, 그리고 요청의 단일 요소만 변형하는 **9,744개 블랙박스 단일 편집 공격 변이(Single-edit variants)**.

| 공격 벡터 / 측정 지표 | 실측 영향도 | 보안 및 운영상 시사점 |
| :--- | :--- | :--- |
| **검증되지 않은 의견 1문장 추가 (Unverified Opinion Appended)** | **12.1% 결정 뒤집힘 (Decision Flip)** | 직접적인 명령 주입(Injected Command, **10.1%**)과 통계적으로 동등한 수준의 치명적 결정 왜곡 유발 |
| **신뢰도 임계값 붕괴 (Confidence Degradation < 0.8)** | **고신뢰 응답의 38%가 0.8 미만으로 하락** | 공격자가 결정을 완전히 뒤집지 못하더라도, 인간 검토(Human Review)나 고비용 상위 모델([[wiki/Agents/Evaluations/Judge-Model-Comparison.md|GPT-6 Cascade]])로 강제 라우팅시켜 **인간 검토 큐 마비(DoS) 및 에스컬레이션 비용 폭탄** 유발 가능 |

---

## 3. `LettuceDetect`: ModernBERT 기반 토큰 수준 RAG 환각 탐지기
결정 모델이 라우팅·판정을 검증한다면, 생성된 RAG 응답의 문맥 정합성(Grounding)은 **LettuceDetect**와 같은 경량 토큰 분류기로 검증한다.
- **아키텍처**: **ModernBERT** 백본(최대 **4K 컨텍스트 윈도우**)을 **RAGTruth** 데이터셋에 파인튜닝한 경량 인코더 모델(MIT 라이선스).
- **핵심 기능**:
  1. **토큰 단위 정밀도(Token-level Precision)**: 응답 전체를 단순 통과/실패로만 판정하는 대신, 제공된 검색 문맥(Context)으로 뒷받침되지 않는 **정확한 환각 스팬(Hallucinated Spans)**을 토큰 단위로 색출한다.
  2. **초저지연 추론 및 간편한 통합**: 대형 LLM Judge 호출 없이 `pip` 설치 및 Hugging Face 1줄 모델 로딩으로 RAG 후처리 파이프라인에 즉시 결합 가능하다.

---

## 4. 자가 개선(RSI) 및 벤치마크 주장에 대한 감사 체크리스트
오픈 모델 카드(예: `Darwin 27B RSI`)나 상용 벤더가 발표하는 벤치마크 점수를 실무 도입 전에 검증할 때 반드시 확인해야 할 3대 감사 규칙이다.

1. **문항 수 환산 및 노이즈 플로어(Noise Floor) 점검**:
   - 예: 198문항으로 구성된 `GPQA Diamond`에서 `+5.24%p` 상승은 실제로는 **약 10.4문항** 차이에 불과하다. 각 평가의 노이즈 플로어(약 ±3%p)를 고려할 때, 문항별 출력(Per-question outputs)과 쌍대 검정(Paired test) $p$-value 원본이 공개되지 않은 주장은 검증 불가(Unverifiable)로 취급해야 한다.
2. **평가 프로토콜 불일치(Incomparable Baselines) 식별**:
   - 동일 연구소의 두 모델 카드에서 동일 198문항에 대해 한쪽(Opus 카드)은 `86.9%`(재시도 + 검증 패스 사용), 다른 쪽(RSI 카드 시작점)은 `72.85%`(단일 샘플 응답)를 보고하는 것처럼 **14%p의 방법론 격차**가 존재할 수 있다. 추론 시점 연산(Retries/Verification) 유무를 통일하지 않은 비교는 무효다.
3. **자가 채점(Self-Grading) 및 비공개 학습 레시피 경계**:
   - *"인간 정답 없이 스스로 개선했다"*고 주장하면서 라운드별 생성 데이터와 보상 판정기(Grader) 구성을 비공개한 경우, 모델이 자체 채점기의 편향을 해킹([[wiki/Models/RL/Post-Training-OPD-and-Sparse-Reward-Dynamics-2026.md|Co-Cheating]])했을 가능성을 배제할 수 없다. 반드시 **독립된 자체 평가 세트**(예: OCR의 경우 벤더 자체 발표치 대신 AllenAI 공식 `olmOCR-bench` 8,413개 테스트 2회 독립 재현)로 재검증해야 한다.

---

## 5. 관련 문서 (Cross-References)
- [[wiki/Agents/Frameworks/TypeSafe-Jev-System-One-Decision-Architecture.md]]
- [[wiki/Models/Optimization-and-Serving/AnyJev-and-Jeva-Decision-Model-Ecosystem.md]]
- [[wiki/Agents/Evaluations/Judge-Model-Comparison.md]]
- [[wiki/Agents/Evaluations/TasteVal-Scientific-Research-Taste-Benchmark.md]]
- [[wiki/RAG/SOTA-OCR-및-문서-정규화-기술.md]]
- [[wiki/Agents/Frameworks/Evaluations/000_Evaluations-MOC.md]]
