---
title: "NVIDIA Object-Oriented Agents (NOOA): 객체 지향형 에이전트 프레임워크"
date: "2026-07-31"
last_updated: "2026-07-31"
updated: "2026-07-31"
related_raw: ["[[2026-07-31-nvidia-oo-agents-framework.md]]"]
tags: ["Agents", "Frameworks", "NOOA", "NVIDIA-Labs", "Object-Oriented"]
type: "wiki"
---

# NVIDIA Object-Oriented Agents (NOOA): 객체 지향형 에이전트 프레임워크

**NVIDIA Object-Oriented Agents (NOOA)**는 NVIDIA Labs에서 발표한 연구(arXiv:2607.20709)로, 에이전트 작동 논리를 특수 프롬프트 템플릿이나 임의의 YAML 설정에 의존하는 대신 **순수 파이썬의 객체 지향 프로그래밍(OOP) 구조**로 나타내고 실행하도록 설계된 프레임워크입니다.

## 1. 핵심 아키텍처 및 철학

- **Code as Schema (코드가 곧 스키마)**: 
  - 에이전트의 **상태(State)**는 객체의 **필드(Fields)**로 관리됩니다.
  - 에이전트의 **행동(Actions)**은 객체의 **메소드(Methods)**로 정의됩니다.
  - 에이전트가 받는 **지침(Instructions)**은 메소드 및 클래스의 **독스트링(Docstrings)**으로 표현됩니다.
  - 에이전트 행위에 대한 **제약 조건(Constraints)**은 파이썬의 **타입 힌트(Type Hints)**를 사용하여 정적/동적으로 검증됩니다.
- **Pass-by-Reference (참조 전달)**: 
  구식 에이전트 프레임워크가 매 루프마다 에이전트 상태를 거대한 텍스트 프롬프트로 직렬화(Serialization)하여 모델에 주입하는 대신, NOOA는 활성 객체에 대한 파이썬 메모리 참조 주소를 직접 넘겨 장기 에이전트 루프 작동 시 토큰 비용을 최소화하고 상태 보존 정밀도를 높입니다.
- **SWE-bench Verified 성과**: 
  이 단순한 OOP 기반 참조 유지 및 엄격한 계약(Contract) 관리는 SWE-bench Verified 벤치마크 및 ARC-AGI-3 평가에서 토큰 비용 대비 성능을 나타내는 파레토 경계(Pareto Frontier)를 크게 앞당겼습니다.

## 2. 코드 스펙 예시

NOOA를 활용해 간단한 파일 탐색 에이전트를 구성하는 예시 코드입니다:

```python
from typing import List
from nooa import OOAgent, action

class CodeBaseAgent(OOAgent):
    """
    당신은 코드베이스를 자율적으로 분석하고 버그를 수정하는 에이전트입니다.
    """
    
    # 에이전트 상태를 멤버 필드로 직접 정의
    search_history: List[str] = []
    current_file: str = ""

    @action
    def read_file(self, file_path: str) -> str:
        """
        지정된 절대 경로의 파일 내용을 읽어옵니다.
        """
        self.current_file = file_path
        self.search_history.append(f"Read {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    @action
    def grep_pattern(self, pattern: str, directory: str) -> List[str]:
        """
        특정 디렉토리 하위에서 패턴을 검색합니다.
        """
        self.search_history.append(f"Grep '{pattern}' in {directory}")
        # 실제 grep 실행 로직...
        return ["file.py:L10 - def find_user():"]
```

## 3. 의의 및 한계 극복

- **개발자 경험(DX) 극대화**: 에이전트를 정의하기 위해 별도의 DSL(Domain Specific Language)이나 템플릿 언어를 배울 필요 없이, 평범한 파이썬 프로그래밍 방식으로 에이전트 스킬과 도구를 작성할 수 있습니다.
- **보안 및 예외 제어**: 메소드 단위의 에이전트 액션을 실행할 때 타입 힌트와 파이썬 런타임 가드레일이 작동하여, 예기치 않은 도구 오작동이나 텍스트 직렬화 에러를 사전에 완벽히 방어합니다.

## 🔗 연결된 문서
- [[wiki/Agents/Frameworks/000_Frameworks-MOC.md]]
- [[wiki/Engineering/Prompt-Engineering/프롬프트 엔지니어링에서 컨텍스트 엔지니어링으로의 전환.md]]
