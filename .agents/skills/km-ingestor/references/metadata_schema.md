# KM Metadata Schema

모든 `raw/` 및 `wiki/` 문서는 Obsidian의 기능(태그, 속성, 그래프 등)을 활용하기 위해 다음의 메타데이터 형식을 준수해야 합니다.

## 원천 소스 (Raw) 문서 스키마

`raw/` 폴더에 저장되는 모든 문서의 상단에 위치합니다.

```yaml
---
title: "문서의 공식 제목"
source: "원본 웹사이트 URL 또는 로컬 파일 경로"
date: "YYYY-MM-DD (수집 날짜)"
author: "원작자 (가능한 경우)"
tags: ["inbox", "주제"] # 주제는 소문자/하이픈 권장
type: "raw"
description: "문서에 대한 한 줄 요약"
---
```

## 지식 위키 (Wiki) 문서 스키마

`wiki/` 폴더에 저장되는 분석, 요약, 개념 노트의 상단에 위치합니다.

```yaml
---
title: "노트 제목"
related_raw: ["[[raw_문서_링크]]"] # 기반이 된 원천 소스들
tags: ["wiki", "개념"]
type: "wiki"
status: "draft/complete/outdated" # 상태 관리
last_updated: "YYYY-MM-DD"
---
```

## 필드 가이드라인
- **tags**: Obsidian 태그 기능과 연동됩니다. 범용적인 태그(inbox, research, theory 등)를 먼저 쓰고, 구체적인 주제 태그를 추가합니다.
- **source**: 웹 수집(`Read`/`Shell`) 결과나 출처 추적에 사용됩니다.
- **related_raw**: 지식의 계보(Lineage)를 파악하기 위해 필수적으로 작성합니다.
