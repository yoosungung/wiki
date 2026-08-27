# LLM API 프로바이더 비용 및 성능 분석

## 핵심 주장 (Claims)
인공지능 모델과 API 프로바이더 생태계를 지능(Intelligence), 속도(Speed), 비용(Cost) 측면에서 분석하여 사용자의 유스케이스에 최적화된 모델을 선택할 수 있도록 돕는 지표를 제공합니다.

## 측정 지표 및 시스템 설계 (Metrics & Methodology)
**주요 분석 지수**:
1. **Artificial Analysis Intelligence Index (지능 지수)**
   - 모델의 전반적인 성능을 평가하는 복합 지수.
   - 포함된 평가 항목: GDPval-AA v2 (실제 업무), 𝜏³-Banking (도구 사용), Terminal-Bench v2.1 (코딩/터미널), SciCode, Humanity's Last Exam (추론 및 지식), GPQA Diamond, CritPt, AA-Omniscience, AA-LCR (긴 문맥 추론) 등.
2. **Speed (속도)**
   - 초당 출력 토큰 수(Output tokens per second).
3. **Cost per Task (작업당 비용)**
   - 지능 지수 테스트를 수행하는 데 드는 가중 평균 비용(USD).
4. **Endpoint Accuracy Index (엔드포인트 정확도 지수)**
   - 프로바이더의 엔드포인트가 참조 모델과 동일한 품질의 결과를 제공하는지 측정.

**특수 목적 에이전트 평가**:
- **Coding Agent Index**: 소프트웨어 엔지니어링 작업(DeepSWE, Terminal-Bench v2 등)의 평균 pass@1 측정.
- **AA-Briefcase**: 스프레드시트, 프레젠테이션, 메모 작성이 필요한 장기 에이전트 지식 워크플로우 성능 평가 (분석 품질 및 프레젠테이션 Elo 포함).
- **AA-Omniscience Index**: 사실적 정확도와 환각(hallucination) 방지 능력을 측정 (정답 보상, 오답 페널티).
- **Openness Index**: 모델의 가용성 및 투명성(구성 요소의 개방 정도) 평가.

## 도입 및 선택 전략
지능 지수와 작업당 비용을 축으로 하는 Pareto 곡선을 통해 비용 대비 가장 효율적인 모델(Most attractive quadrant)을 추천받고, 필요에 따라 속도(Output Token/s)를 최우선으로 고려한 프로바이더를 선택할 수 있습니다.
