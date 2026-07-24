---
title: "Chonkie TableChunker: RAG 성능 향상을 위한 표 데이터 최적화 청커"
related_raw: ["[[2026-07-24-chonkie-tablechunker-for-rag.md]]"]
tags: ["RAG", "Chunking", "Text-Processing", "Tables", "Chonkie"]
type: "wiki"
status: "published"
last_updated: "2026-07-24"
updated: "2026-07-24"
---

# Chonkie TableChunker: RAG 성능 향상을 위한 표 데이터 최적화 청커

## 1. 개요
[Chonkie](https://github.com/bhavnicksm/chonkie)는 RAG(Retrieval-Augmented Generation) 파이프라인의 속도와 경량화를 목표로 설계된 오픈소스 텍스트 청킹(Text Chunking) 라이브러리입니다. 그중 **`TableChunker`**는 마크다운(Markdown) 및 HTML 문서 내의 표(Table) 데이터를 분할할 때, 셀이 잘려 나가거나 행 구조가 유실되어 LLM이 표의 문맥을 잃어버리는 문제를 해결해주는 전용 청킹 모듈입니다.

## 2. TableChunker 핵심 아키텍처
기존의 일반적인 텍스트 분할 방식(예: 문자 수 기준 또는 재귀적 분할)은 표 데이터를 임의의 위치에서 잘라내기 때문에 테이블 헤더가 유실되거나 행 중간이 분단되는 현상이 잦았습니다. `TableChunker`는 이를 극복하기 위해 다음 기법을 활용합니다:

- **구조 인식형 행 단위 분할 (Structure-Aware Row Splitting):** 표의 외곽선(Boundary)을 감지하고, 행(Row) 단위를 유지하며 청크를 분리합니다.
- **헤더 반복 주입 (Header Replication):** 하나의 큰 표가 여러 개의 청크로 쪼개질 때, 각 청크의 시작 부분에 표의 **열 제목(Header Row)을 자동으로 복제**하여 주입합니다. 이를 통해 각 청크가 독립된 텍스트로 벡터 스페이스에 임베딩되더라도 열의 맥락을 완벽히 유지합니다.

```markdown
[원본 거대 표] -> 쪼개짐
청크 1: [헤더] + [1행~10행]
청크 2: [헤더] + [11행~20행] (자동으로 헤더 복제 주입)
```

## 3. 기술적 구현 및 예시 코드 (Python)
파이썬 환경에서 `TableChunker`를 구동하는 상세 가이드입니다.

### 설치
```bash
pip install chonkie
```

### 파이썬 실행 예시
```python
from chonkie import TableChunker

# 1. 샘플 마크다운 데이터 (텍스트와 표 혼합)
markdown_doc = """
# 2026년 NPU 라인업 비교
아래는 주요 NPU 칩의 세부 명세입니다.

| NPU 이름 | 개발사 | 공정 (nm) | 메모리 스택 |
| :--- | :--- | :--- | :--- |
| RNGD | FuriosaAI | 5 | 48GB HBM3 |
| ATOM-Max | Rebellions | 5 | 64GB HBM3 |
| Stork | FuriosaAI | 2 | 96GB HBM4 |
| Panther Lake | Intel | 18A | LPDDR5X (UMA) |
"""

# 2. TableChunker 초기화 (청크 크기 및 겹침 범위 설정)
# chunk_size는 토큰 단위 임계점입니다.
chunker = TableChunker(chunk_size=100, overlap=10)

# 3. 청킹 실행
chunks = chunker(markdown_doc)

# 4. 결과 출력
for idx, chunk in enumerate(chunks):
    print(f"--- Chunk {idx+1} ---")
    print(chunk.text)
```

## 관련 문서
- [[wiki/RAG/000_RAG-MOC.md|RAG 기술 인덱스 MOC]]
- [[wiki/Engineering/AI-Native-Engineering/Claude-Code-Karpathy-Guidelines.md|Claude Code 및 에이전트 지침]]
