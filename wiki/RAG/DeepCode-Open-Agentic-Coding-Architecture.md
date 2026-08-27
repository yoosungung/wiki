# DeepCode: 오픈 에이전트 코딩 아키텍처

## 핵심 주장 (Claims)
DeepCode는 단순한 코드 스니펫 생성을 넘어 실제 소프트웨어 엔지니어링 프로젝트를 이해하고, 수정하고, 테스트하고, 검증하는 범용 오픈소스 코딩 에이전트 프레임워크입니다. Paper2Code(논문을 코드로 변환)와 같은 복잡한 연구 재현 작업뿐만 아니라 텍스트 기반의 웹/백엔드 개발을 지원합니다.

## 시스템 구조 및 설계 (Architecture & Design)
DeepCode의 "Deep"은 다음 4가지 핵심 깊이를 의미합니다:
1. **Deep Context (깊은 문맥)**: 프로젝트 구조, 엔지니어링 규칙, 세션 기록 및 장기 메모리를 통한 작업 이해.
2. **Deep Execution (깊은 실행)**: 코드 검색, 편집, 커맨드 및 테스트 실행을 통해 단순한 제안이 아닌 실제 결과물을 도출.
3. **Deep Verification (깊은 검증)**: 테스트 결과, 빌드 출력, 정적 검사 및 Diff를 기반으로 작업의 성공 여부를 검증.
4. **Deep Continuity (깊은 연속성)**: 디렉토리, 클라이언트, 모델 변경을 가로질러 대화, 도구 기록, 결정 사항을 보존.

**Paper2Code 파이프라인**:
- **의도 이해 (Intent Understanding)**: 사용자 목표를 기술적 제약과 작업 분할로 변환.
- **문서 파싱 (Document Parsing)**: 논문/문서에서 알고리즘, 수식, 구현 요구사항 추출.
- **코드 계획 (Code Planning)**: 구현 로드맵 및 모듈 경계 설정.
- **코드 참조 마이닝 및 인덱싱 (Reference Mining & Indexing)**: 관련 저장소 검색 및 의미론적 그래프 구축 (CodeRAG).
- **코드 생성 및 검증 (Code Generation & Verification)**: 실행 가능한 코드 생성 및 반복적인 피드백을 통한 수정.

## API 스펙 및 CLI 커맨드
**DeepCode CLI 설치 및 초기화**:
```bash
uv tool install --python 3.12 deepcode-hku
deepcode init
```

**모델 프로바이더 설정**:
```bash
deepcode provider set personal-openrouter --template openrouter --label "OpenRouter · Personal" --api-key
deepcode provider models personal-openrouter --refresh
```

**작업 디렉토리에서 에이전트 실행**:
```bash
cd <your-project>
deepcode
```

**인터랙티브 CLI 명령어**:
- `/new [title]`: 새 세션 시작
- `/resume`: 로컬 히스토리 재개
- `/model`: 다음 턴의 모델 변경
- `/effort`: 모델의 사고(Thinking) 수준 조정
- `/permissions`: 도구 접근 권한(허용/묻기/거부) 설정
- `/goal`: 장기 목표 설정 및 관리
