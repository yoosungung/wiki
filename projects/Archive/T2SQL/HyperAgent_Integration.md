# HyperAgent 기반 T2SQL 자가 진화 프레임워크 통합 계획

이 문서는 `yoosungung/nl2sql-deep` 프로젝트의 Phase 11(Agent View) 및 Phase 12(시멘틱 레이어 최적화) 단계에 `HyperAgent`의 재귀적 자기 개선 메커니즘을 통합하는 전략을 다룹니다.

## 1. Private Repository 접근 및 환경 설정

본 프로젝트는 Private 저장소이므로, AI 에이전트나 외부 도구에서 접근 시 로컬에 인증된 `gh` (GitHub CLI)를 활용합니다.

### GitHub CLI (`gh`) 활용법
- **저장소 정보 확인**: `gh repo view yoosungung/nl2sql-deep --json name,description,visibility`
- **파일 목록 및 내용 조회 (API 활용)**:
  - 루트 목록: `gh api repos/yoosungung/nl2sql-deep/contents/ -q '.[].path'`
  - 특정 파일 읽기: `gh api repos/yoosungung/nl2sql-deep/contents/PLANS.md -q '.content' | base64 --decode`
- **로컬 작업**: `git clone` 후 로컬 인증 정보를 사용하여 `git` 명령어로 상호작용 가능.

---

## 2. HyperAgent 적용 핵심 전략

### A. Agent View Generation의 자가 개선 (Hyper-Loop)
- **개념**: `PLANS.md`의 Phase 11에서 청크별 CTE 생성 시 발생하는 반복적 실패 패턴을 에이전트가 스스로 학습.
- **적용**: `generate_agent_view` 도구가 에러 발생 시 `Trace`를 분석하여 해당 스키마 청크에 특화된 **"Chunk-specific Guidance"**를 생성하고 `agent_views/` 캐시에 저장하여 다음 시도에 자동 반영.

### B. DGM-H 방식의 Composer Subagent
- **개념**: 최종 SQL을 조립하는 Composer에게 자신의 조립 로직과 최적화 전략을 수정할 권한 부여.
- **적용**: DB의 `EXPLAIN` 결과를 피드백으로 받아 Join 순서나 최적화 힌트(Index Hint 등) 생성 전략을 실시간 리팩토링. `src/nl2sql_pipeline/chunking.py` 내의 전략 Hook을 에이전트가 직접 제어.

### C. 시멘틱 레이어의 자가 진화 (Semantic Evolution)
- **개념**: SQL 생성 과정에서 발견된 암시적 지식을 시멘틱 YAML에 반영 (Phase 12 확장).
- **적용**: 에이전트가 높은 신뢰도로 생성한 SQL 로직에서 추출한 "테이블 간 숨겨진 관계"나 "비즈니스 규칙"을 `/semantic/tables/`의 `business_rules` 필드에 스스로 제안/업데이트.

### D. Hyper-Repair 시스템
- **개념**: `sqlglot` 기반의 단순 구문 수정을 넘어선 메타 분석 기반의 복구.
- **적용**: 에러 발생 원인에 대한 "메타 리포트"를 생성하고, 이를 바탕으로 `nl2sql_deep/tools/sql_safety.py`의 검증 규칙을 샌드박스 내에서 일시적으로 확장하거나 수정하여 테스트.

---

## 3. 향후 구현 단계 (Next Steps)

1. **Schema 모델 확장**: `src/nl2sql_pipeline/semantic/schema.py`에 `SelfImprovementLog` 및 `AgentViewGuidance` 모델 추가.
2. **Subagent 프로토타이핑**: `view-generator` subagent가 실패 시 스스로 프롬프트를 수정하는 로직 구현.
3. **Evaluation Pipeline 통합**: `Opik`(Phase 8)의 평가 점수를 `HyperAgent`의 진화 트리거(Evolution Trigger)로 활용.

---
*참조: 이 계획은 `PLANS.md`의 Phase 11 및 12와 긴밀히 연동되어 수행되어야 함.*
