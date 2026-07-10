---
related_raw: ["[[2026-06-25-omniparse_Ingest_Parse_Optimize_Data_Formats.md]]"]
tags: ["#wiki", "omniparse", "Data-Parsing", "RAG-Ingestion", "Multi-Format"]
---

# omniparse: 멀티포맷 데이터 정규화 및 파싱 파이프라인

**omniparse**는 텍스트 문서, 복잡한 표, 오디오, 이미지, 비디오 등 기업 내부의 비정형 멀티포맷 데이터를 AI 에이전트가 활용하기 가장 쉬운 기계 가독성 표준 마크다운(Markdown) 포맷으로 전처리 및 정규화(Ingestion & Optimization)해 주는 올인원 파이프라인 솔루션입니다.

## 1. 주요 핵심 기능
- **전방위 멀티포맷 대응**: 단순한 스캔 PDF나 워드 파일 파싱에 머무르지 않고, 영상 프레임 캡셔닝, 오디오 음성 전사(STT) 정보 등 복합 멀티미디어를 시맨틱 구조화 마크다운으로 일괄 용융해 냅니다.
- **에이전트 호환성 극대화**: 에이전트가 구조적 파싱 에러를 유발하기 쉬운 HTML, PDF 테이블 등을 최적화된 테이블 마크다운 및 이미지 바운딩 링크로 정리하여 문맥 전달력을 높입니다.
- **로컬 보안 처리**: 모든 전처리 엔진이 로컬 자원(GPU/CPU)을 사용하므로, 민감한 환자 정보나 기밀 기업 문서를 외부 클라우드 API로 송출할 필요가 없어 높은 정보 보안 수준을 유지합니다.

## 🔗 연결된 문서
- [[wiki/RAG/SOTA-OCR-및-문서-정규화-기술.md]] — SOTA OCR 엔진과의 결합.
- [[wiki/RAG/000_RAG-MOC.md]]
