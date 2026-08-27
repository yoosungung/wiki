# Docling: 문서를 지식 그래프로 변환

## 핵심 주장 (Claims)
Docling Graph는 PDF, 이미지, Markdown 등 비정형 문서를 Pydantic 객체로 추출한 뒤, 의미론적 관계가 명확한 방향성 지식 그래프(Knowledge Graph)로 변환하는 도구입니다. 대략적인 텍스트 임베딩(RAG)에 의존하는 대신 화학, 금융, 법률 분야처럼 정확한 엔티티 연결이 필요한 곳에 적합합니다.

## 시스템 구조 및 파이프라인 (Architecture)
- **추출 파이프라인**: 
  - **VLM 백엔드**: 로컬 Docling VLM 인퍼런스.
  - **LLM 백엔드**: LiteLLM을 통해 로컬(vLLM, Ollama) 및 원격 API(OpenAI, Gemini 등) 지원.
  - 뼈대 추출 후 살붙이기(skeleton-then-flesh) 방식의 덴스(Dense) 추출 모드 지원.
- **Pydantic 템플릿**: 추출 스키마와 그래프 구조를 동시에 정의. 엔티티 간의 엣지(Edge)를 명시적으로 선언.
- **그래프 및 검증**: 생성된 Pydantic 모델을 NetworkX 방향성 그래프로 변환. LLM 추가 호출 없이 소스 청크와 페이지 바운딩 박스를 가리키는 출처(Provenance) 데이터 매핑 지원.
- **내보내기 및 시각화**: CSV, Cypher 형식으로 내보내거나 대화형 HTML/Markdown 리포트로 시각화. 여러 지식 그래프의 안전한 병합(Graph Fusion) 지원.

## API 스펙 및 CLI 커맨드
**설치**:
```bash
pip install docling-graph
pip install "docling-graph[vlm]" # VLM 백엔드 지원 추가
```

**CLI를 통한 변환 및 시각화**:
```bash
# 초기화
docling-graph init

# URL 문서를 지식 그래프로 변환 (추출 템플릿 지정)
docling-graph convert "https://arxiv.org/pdf/2207.02720" \
    --template "docs.examples.templates.rheology_research.ScholarlyRheologyPaper" \
    --processing-mode "many-to-one" \
    --extraction-contract "dense" \
    --debug

# 결과 시각화 검사
docling-graph inspect outputs
```

**문서에서 템플릿 자동 생성 (Schema Induction)**:
```bash
docling-graph template from-docs invoice1.pdf invoice2.pdf \
    --output templates/invoices.py \
    --name InvoiceDocument \
    --trial-run
```
